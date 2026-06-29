from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
class TaskCreate(BaseModel):
    title: str
    done: bool = False


class TaskResponse(BaseModel):
    id: int
    title: str
    done: bool

    class Config:
        from_attributes = True


@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(title=task.title, done=task.done)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)   #here we refresh to get the auto generated id 
    return new_task

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

@app.get("/tasks/{id}", response_model=TaskResponse)
def get_task(id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {id} not found.")
    return task


@app.put("/tasks/{id}", response_model=TaskResponse)
def update_task(id: int, task: TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail=f"Task {id} not found.")
    db_task.title = task.title
    db_task.done  = task.done
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{id}")
def delete_task(id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {id} not found.")
    db.delete(task)
    db.commit()
    return {"message": f"Task '{task.title}' deleted."}