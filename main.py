from fastapi import FastAPI, Depends
import crud
from sqlalchemy.orm import Session
from security import get_current_user
import model
import schemas

import auth

from database import engine,Base
print(Base.metadata.tables.keys())
Base.metadata.create_all(bind=engine)


app = FastAPI()
@app.get("/")
def home():
    return {"message": "API Running 🚀", "go_to_docs": "/docs"}


app.include_router(auth.router)
@app.post("/tasks")
def create_task(

    task: schemas.TaskCreate,

    db: Session = Depends(auth.get_db),

    current_user=Depends(get_current_user)

):

    return crud.create_task(
        db,
        task,
        current_user.id
    )
@app.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(
    db: Session = Depends(auth.get_db),
    current_user = Depends(get_current_user)
):
    return crud.get_tasks(db,current_user.id)
@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task: schemas.TaskCreate,
    db: Session = Depends(auth.get_db),
    current_user=Depends(get_current_user)
):
    return crud.update_task(
        db,
        task_id,
        task
    )
@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(auth.get_db),
    current_user = Depends(get_current_user)
):
    return crud.delete_task(
        db,
        task_id
    )