from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    description: str
    project_id: int

class TaskResponse(BaseModel):
    id: int
    title: str
    priority: str
    due_date_hint: Optional[str] = None
    project_id: int

model_config = {"from_attributes": True}