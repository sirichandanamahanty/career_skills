import os
from typing import Optional, List, Dict, Any
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse

from models import (
    AssessmentRequest,
    AssessmentResponse,
    CustomRoleAIRequest,
    MentorChatRequest,
    MentorChatResponse,
    ProgressSyncRequest
)
from career_data import FIELDS, ROLES_CATALOG, FREE
from analyzer import perform_assessment
from ai_service import (
    generate_custom_profession_ai,
    chat_with_career_mentor
)

app = FastAPI(
    title="Career Skill Gap AI — Backend API",
    description="Universal Career Intelligence & Roadmap Engine supporting 85+ global and Indian careers.",
    version="3.0.0"
)

# Enable CORS for browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

USER_PROGRESS_STORE: Dict[str, Dict[str, Any]] = {}

INDEX_HTML_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "index.html"))


# ==========================================
# 1. FRONTEND WEB APP & HEALTH ENDPOINTS
# ==========================================

@app.get("/")
def serve_frontend():
    """Serves the Career Skill Gap AI frontend web application."""
    if os.path.exists(INDEX_HTML_PATH):
        return FileResponse(INDEX_HTML_PATH, media_type="text/html")
    return {
        "status": "online",
        "service": "Career Skill Gap AI",
        "docs_url": "/docs"
    }


@app.get("/api/health")
def health():
    return {
        "status": "online",
        "service": "Career Skill Gap AI",
        "total_roles_available": len(ROLES_CATALOG),
        "total_fields_available": len(FIELDS),
        "docs_url": "/docs"
    }


# ==========================================
# 2. CAREER CATALOG ENDPOINTS
# ==========================================

@app.get("/api/fields")
def get_fields_of_study():
    """Returns all supported fields of study and their career starting advantages."""
    return [{"field": k, "advantage": v} for k, v in FIELDS.items()]


@app.get("/api/roles")
def get_roles(
    q: Optional[str] = Query(None, description="Search term for role name or description"),
    fs: Optional[str] = Query(None, description="Sector: P (Public) or V (Private)"),
    fr: Optional[str] = Query(None, description="Region: I (India) or A (Abroad)"),
    category: Optional[str] = Query(None, description="Filter by domain category")
):
    """Returns filtered career roles across sectors and regions."""
    roles = list(ROLES_CATALOG.values())

    if q:
        query = q.lower()
        roles = [r for r in roles if query in r["name"].lower() or query in r["description"].lower()]

    if fs:
        roles = [r for r in roles if fs in r["tag"]]

    if fr:
        roles = [r for r in roles if fr in r["tag"]]

    if category:
        roles = [r for r in roles if r["category"] == category]

    return [
        {
            "id": r["id"],
            "name": r["name"],
            "description": r["description"],
            "category": r["category"],
            "sector": r["sector"],
            "region": r["region"],
            "tag": r["tag"],
            "skills_count": len(r["skills"])
        }
        for r in roles
    ]


@app.get("/api/roles/{role_id}")
def get_role_details(role_id: str):
    """Returns complete syllabus, skills, projects, and certifications for a role."""
    if role_id not in ROLES_CATALOG:
        raise HTTPException(status_code=404, detail=f"Role '{role_id}' not found.")
    return ROLES_CATALOG[role_id]


# ==========================================
# 3. ANALYSIS & ROADMAP ENGINE
# ==========================================

@app.post("/api/assess", response_model=AssessmentResponse)
def assess_candidate(req: AssessmentRequest):
    """
    Computes exact weighted readiness score (%), identifies critical skill gaps,
    and generates adaptive week-by-week roadmap based on study hours.
    """
    if req.role_id not in ROLES_CATALOG:
        raise HTTPException(status_code=404, detail=f"Role '{req.role_id}' not found.")
    return perform_assessment(req)


# ==========================================
# 4. AI CUSTOM ROLE & MENTOR ASSISTANT
# ==========================================

@app.post("/api/ai/custom-role")
def create_custom_role_ai(req: CustomRoleAIRequest):
    """
    Uses Gemini AI (with heuristic fallback) to design a full career syllabus
    for ANY unlisted profession.
    """
    generated = generate_custom_profession_ai(req)
    ROLES_CATALOG[generated["id"]] = generated
    return generated


@app.post("/api/ai/ask-mentor", response_model=MentorChatResponse)
def ask_career_mentor(req: MentorChatRequest):
    """
    AI Career Counselor addressing aspirant questions grounded in their deficits and pacing.
    """
    return chat_with_career_mentor(req)


# ==========================================
# 5. USER PROGRESS PERSISTENCE
# ==========================================

@app.post("/api/progress/save")
def save_progress(req: ProgressSyncRequest):
    """
    Saves student progress and checked-off roadmap steps.
    """
    key = req.student_name.strip().lower() or "anonymous"
    USER_PROGRESS_STORE[key] = {
        "student_name": req.student_name,
        "role_id": req.role_id,
        "completed_step_ids": req.completed_step_ids,
        "hours_per_week": req.hours_per_week
    }
    return {"status": "success", "message": f"Progress saved for {req.student_name}"}


@app.get("/api/progress/{student_name}")
def get_progress(student_name: str):
    """
    Retrieves stored progress for a student.
    """
    key = student_name.strip().lower()
    return {"found": key in USER_PROGRESS_STORE, "data": USER_PROGRESS_STORE.get(key)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
