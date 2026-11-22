import math
from typing import Dict, Any, List
from models import (
    AssessmentRequest,
    AssessmentResponse,
    SkillGapItem,
    RoadmapStepItem
)
from career_data import FIELDS, ROLES_CATALOG, FREE


def perform_assessment(
    req: AssessmentRequest,
    custom_role_data: Dict[str, Any] = None
) -> AssessmentResponse:
    hrs = max(2, min(60, req.hours_per_week or 10))
    role = custom_role_data or ROLES_CATALOG.get(req.role_id, ROLES_CATALOG["dev"])
    
    ratings = req.skill_ratings or {}
    
    tot = 0
    got = 0
    raw_gaps = []
    
    # Calculate weighted readiness score
    for i, s in enumerate(role["skills"]):
        weight = s[1]
        hours = s[2]
        # Rating level: 0 (None), 1 (Basic), 2 (Good)
        level = ratings.get(str(i), ratings.get(i, 0))
        level = max(0, min(2, int(level)))
        
        tot += weight
        got += weight * (level / 2.0)
        
        if level < 2:
            raw_gaps.append({
                "index": i,
                "name": s[0],
                "weight": weight,
                "hours": hours,
                "note": s[3] if len(s) > 3 else "",
                "level": level,
                "importance": weight * (2 - level)
            })
            
    score = round((got / tot * 100)) if tot > 0 else 0
    
    if score >= 70:
        score_msg = "You are close. Polish the gaps and start applying."
    elif score >= 35:
        score_msg = "Good base. Work through the roadmap in order."
    else:
        score_msg = "You are at the start, and that is fine. The roadmap below starts from the basics."
        
    fld = req.field or "Computer Science / IT"
    field_adv = FIELDS.get(fld, "Start from the basics in the roadmap and track each step. Consistency matters more than your starting point.")
    
    # Sort gaps by importance descending
    raw_gaps.sort(key=lambda g: g["importance"], reverse=True)
    
    gap_items = [
        SkillGapItem(
            skill_name=g["name"],
            level=g["level"],
            status_label="Needs strengthening" if g["level"] == 1 else "Not started",
            weight=g["weight"],
            hours=g["hours"]
        )
        for g in raw_gaps
    ]
    
    # Build sequential week-by-week roadmap
    roadmap_steps: List[RoadmapStepItem] = []
    cum = 0
    
    for g in raw_gaps:
        step_hours = round(g["hours"] * (0.5 if g["level"] == 1 else 1.0))
        cum_before = cum
        cum += step_hours
        
        a = math.ceil(cum_before / hrs) + 1
        b = math.ceil(cum / hrs)
        if b < a:
            b = a
            
        week_label = f"Week {a}" if a == b else f"Weeks {a}–{b}"
        step_id = f"{role['id']}_{g['index']}"
        
        roadmap_steps.append(
            RoadmapStepItem(
                id=step_id,
                title=g["name"],
                hours=step_hours,
                note=g["note"],
                level=g["level"],
                week_start=a,
                week_end=b,
                week_label=week_label,
                is_completed=False
            )
        )
        
    total_hours = sum(s.hours for s in roadmap_steps)
    total_weeks = math.ceil(total_hours / hrs) if hrs > 0 else 0
    
    if roadmap_steps:
        next_action = f"Start with {roadmap_steps[0].title} this week. Spend {min(hrs, roadmap_steps[0].hours)} hours on it."
    else:
        next_action = "Build your first project and share it publicly."
        
    # Free learning links
    cat_free = FREE.get(role["category"], [])
    all_free = FREE.get("all", [])
    free_links = [
        {"name": item[0], "url": item[1], "description": item[2]}
        for item in (cat_free + all_free)
    ]
    
    return AssessmentResponse(
        name=req.name or "Aspirant",
        role_id=role["id"],
        role_name=role["name"],
        readiness_score=score,
        score_message=score_msg,
        field_advantage=field_adv,
        gaps=gap_items[:5],  # Top 5 most critical
        roadmap=roadmap_steps,
        total_hours=total_hours,
        total_weeks=total_weeks,
        hours_per_week=hrs,
        projects=role.get("projects", []),
        certificates=role.get("certificates", []),
        needs=role.get("needs", []),
        free_learning_resources=free_links,
        books=role.get("books", []),
        next_action=next_action
    )
