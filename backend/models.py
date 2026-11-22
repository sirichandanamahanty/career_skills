from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field


class SkillItem(BaseModel):
    name: str
    weight: int
    hours: int
    note: str


class RoleItem(BaseModel):
    id: str
    name: str
    description: str
    category: str
    skills: List[SkillItem]
    projects: List[str]
    certificates: List[str]
    books: List[str] = Field(default_factory=list)
    needs: List[str] = Field(default_factory=list)
    sector: str = "Public + Private"
    region: str = "India + Abroad"
    tag: str = "PVIA"


class RoadmapStepItem(BaseModel):
    id: str
    title: str
    hours: int
    note: str
    level: int  # 0: None, 1: Basic, 2: Good
    week_start: int
    week_end: int
    week_label: str
    is_completed: bool = False


class SkillGapItem(BaseModel):
    skill_name: str
    level: int  # 0 or 1
    status_label: str  # "Not started" or "Needs strengthening"
    weight: int
    hours: int


class AssessmentRequest(BaseModel):
    name: Optional[str] = ""
    field: Optional[str] = "Computer Science / IT"
    year: Optional[str] = "Second year"
    hours_per_week: int = 10
    role_id: str
    skill_ratings: Dict[str, int] = Field(default_factory=dict)  # skill_index -> 0 (None), 1 (Basic), 2 (Good)


class AssessmentResponse(BaseModel):
    name: str
    role_id: str
    role_name: str
    readiness_score: int
    score_message: str
    field_advantage: str
    gaps: List[SkillGapItem]
    roadmap: List[RoadmapStepItem]
    total_hours: int
    total_weeks: int
    hours_per_week: int
    projects: List[str]
    certificates: List[str]
    needs: List[str]
    free_learning_resources: List[Dict[str, str]]
    books: List[str]
    next_action: str


class CustomRoleAIRequest(BaseModel):
    profession_name: str
    key_skills_text: Optional[str] = ""
    category: Optional[str] = "Specialized Careers"


class MentorChatRequest(BaseModel):
    question: str
    role_name: str
    readiness_score: int
    top_gaps: List[str] = Field(default_factory=list)
    hours_per_week: int = 10


class MentorChatResponse(BaseModel):
    answer: str
    key_takeaways: List[str] = Field(default_factory=list)


class ProgressSyncRequest(BaseModel):
    student_name: str
    role_id: str
    completed_step_ids: List[str]
    hours_per_week: int
