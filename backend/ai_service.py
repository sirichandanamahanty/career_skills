import os
import json
from typing import Dict, Any, List
from models import CustomRoleAIRequest, MentorChatRequest, MentorChatResponse

# Optional Google Generative AI
try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
if HAS_GENAI and GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)


def generate_custom_profession_ai(req: CustomRoleAIRequest) -> Dict[str, Any]:
    """
    Dynamically generates a full structured role definition for ANY custom profession:
    skills with weights, hours, notes, portfolio projects, certifications, books, and prerequisites.
    """
    role_name = req.profession_name.strip()
    slug = "custom_" + role_name.lower().replace(" ", "_")[:20]

    if HAS_GENAI and GEMINI_API_KEY:
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"""
            You are an expert career counselor and curriculum architect.
            Generate a comprehensive career profile for:
            Profession: {role_name}
            Category: {req.category}
            User Suggested Skills: {req.key_skills_text}

            Return ONLY valid JSON matching this exact structure:
            {{
                "id": "{slug}",
                "name": "{role_name}",
                "description": "Short 1-sentence career description",
                "category": "{req.category}",
                "skills": [
                    ["Skill Name", 10, 30, "What to learn and why"],
                    ["Skill Name 2", 12, 40, "What to learn and why"],
                    ["Skill Name 3", 8, 25, "What to learn and why"],
                    ["Skill Name 4", 9, 20, "What to learn and why"],
                    ["Skill Name 5", 7, 20, "What to learn and why"]
                ],
                "projects": [
                    "Portfolio project 1",
                    "Portfolio project 2",
                    "Portfolio project 3"
                ],
                "certificates": [
                    "Recognized certification or exam 1",
                    "Recognized certification or exam 2"
                ],
                "books": [
                    "Standard Reference Book 1",
                    "Standard Reference Book 2"
                ],
                "needs": [
                    "Entry: degree or entry requirement",
                    "Tools: essential tools and software",
                    "Also: portfolio or licensing advice"
                ],
                "sector": "Public + Private",
                "region": "India + Abroad",
                "tag": "PVIA"
            }}
            Ensure skills has 5 to 8 skills, weights between 6 and 14, hours between 10 and 80.
            """
            res = model.generate_content(prompt)
            clean_text = res.text.strip()
            if clean_text.startswith("```json"):
                clean_text = clean_text[7:]
            if clean_text.endswith("```"):
                clean_text = clean_text[:-3]
            data = json.loads(clean_text.strip())
            return data
        except Exception as e:
            print(f"Gemini custom role generation error: {e}")

    # Fallback generator if offline or API key not present
    user_skills_list = [s.strip() for s in (req.key_skills_text or "").split("\n") if s.strip()]
    if not user_skills_list:
        user_skills_list = [
            f"{role_name} Fundamentals & Theory",
            "Core Tools & Techniques",
            "Applied Problem Solving",
            "Quality, Standards & Compliance",
            "Portfolio Project Execution"
        ]

    skills = []
    for i, s_title in enumerate(user_skills_list[:8]):
        weight = 12 - min(i, 4)
        hours = 25 + (i % 3) * 10
        note = f"Core competency in {s_title}"
        skills.append([s_title, weight, hours, note])

    return {
        "id": slug,
        "name": role_name,
        "description": f"Master competencies for {role_name}",
        "category": req.category or "Specialized Careers",
        "skills": skills,
        "projects": [
            f"Build a showcase portfolio project demonstrating {role_name} skills",
            "Solve an end-to-end case study from the field",
            "Present your work to an industry mentor for review"
        ],
        "certificates": [
            f"Professional certification in {role_name}",
            "Industry standard coursework and licensing"
        ],
        "books": [
            f"The Handbook of {role_name}",
            "Professional Practice and Standards"
        ],
        "needs": [
            "Entry: check the official degree or portfolio requirements",
            "Tools: standard industry equipment and software",
            "Also: proof of work and strong practical portfolio"
        ],
        "sector": "Public + Private",
        "region": "India + Abroad",
        "tag": "PVIA"
    }


def chat_with_career_mentor(req: MentorChatRequest) -> MentorChatResponse:
    """
    AI Career Counselor responding to aspirant questions based on their exact readiness and gaps.
    """
    if HAS_GENAI and GEMINI_API_KEY:
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"""
            You are a wise, practical career mentor.
            The user is preparing for: {req.role_name}
            Current Readiness Score: {req.readiness_score}%
            Available Study Time: {req.hours_per_week} hours/week
            Their biggest skill gaps: {', '.join(req.top_gaps) if req.top_gaps else 'None, ready to apply'}

            User Question: "{req.question}"

            Give an encouraging, realistic 2-3 paragraph answer with specific actionable steps.
            """
            res = model.generate_content(prompt)
            return MentorChatResponse(
                answer=res.text.strip(),
                key_takeaways=[
                    f"Focus first on: {req.top_gaps[0] if req.top_gaps else 'Interview practice'}",
                    f"Protect your {req.hours_per_week} hours/week study block",
                    "Build projects to prove competency"
                ]
            )
        except Exception as e:
            print(f"Gemini mentor chat error: {e}")

    # Fallback mentor answer
    top_gap_str = req.top_gaps[0] if req.top_gaps else "core projects"
    return MentorChatResponse(
        answer=(
            f"To reach 80%+ readiness in **{req.role_name}** with **{req.hours_per_week} hours/week**:\n\n"
            f"1. **Tackle your biggest gap first:** Spend your upcoming study blocks on **{top_gap_str}**. "
            f"Split your weekly {req.hours_per_week} hours into two 3-hour deep work sessions on weekends and 1-hour weekday reviews.\n\n"
            f"2. **Proof of work:** Don't just read books or watch videos. Build one concrete deliverable or project from the roadmap each month."
        ),
        key_takeaways=[
            f"Target: {top_gap_str}",
            f"Schedule: {req.hours_per_week} hrs/week consistency",
            "Active recall over passive watching"
        ]
    )
