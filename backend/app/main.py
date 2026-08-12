from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database
from .parser import mock_llm_parser

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/tasks/quick-add", response_model=schemas.TaskResponse, status_code=201)
def quick_add(task_data: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    parsed = mock_llm_parser(task_data.description)
    
    new_task = models.Task(
        title=parsed["title"],
        priority=parsed["priority"],
        due_date_hint=parsed["due_date_hint"],
        project_id=task_data.project_id
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task