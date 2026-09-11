
from sqlalchemy.orm import Session
import model
import schemas
from security import hash_password


def create_user(db: Session, user: schemas.UserCreate):

    hashed_password = hash_password(user.password)

    db_user = model.User(
        username=user.username,
        password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
def get_user_by_username(db: Session, username: str):

    return db.query(model.User).filter(
        model.User.username == username
    ).first()
def create_task(db: Session, task: schemas.TaskCreate, user_id: int):

    db_task = model.Task(
        title=task.title,
        description=task.description,
        owner_id=user_id
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

def get_tasks(db: Session, user_id: int):
    return db.query(model.Task).filter(
        model.Task.owner_id == user_id
    ).all()

def delete_task(db: Session, task_id: int):

    task = db.query(model.Task).filter(
        model.Task.id == task_id
    ).first()

    if task:
        db.delete(task)
        db.commit()

    return task
def update_task(db: Session, task_id: int, task: schemas.TaskCreate):

    db_task = db.query(model.Task).filter(
        model.Task.id == task_id
    ).first()

    if db_task:
        db_task.title = task.title
        db_task.description = task.description

        db.commit()
        db.refresh(db_task)

    return db_task

