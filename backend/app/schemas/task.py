from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: TaskStatus = TaskStatus.PENDING
    
    
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus
    created_at: datetime
    due_date: Optional[datetime] = None
    user_id: int
    
    class Config:
        orm_mode = True