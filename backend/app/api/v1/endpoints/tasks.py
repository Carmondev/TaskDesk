from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.task import Task, TaskCreate
from app.crud import task as crud_task
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db)):
    return crud_task.get_tasks(db)

@router.post("/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crud_task.create_task(db, task)
