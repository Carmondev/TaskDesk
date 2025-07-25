from sqlalchemy import Column, Integer, String, ForeignKey
from
from app.database import Base
from datetime import datetime
import enum

class TaskStatus(str, enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    
class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, default=TaskStatus.PENDING.value, nullable=False)
    created_at = Column(datetime, default=datetime.utcnow)
    due_date = Column(datetime, nullable=True)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")