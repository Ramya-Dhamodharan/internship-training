from fastapi import FastAPI
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my first FastAPI app!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}! Welcome to FastAPI."}

@app.get("/Hello/{name}/{Password}")
def test(name:str, password=1234):
    return{"message":f"Hello {name}."}


students = {}


@app.get("/students/{student_id}")
def get_student(student_id: int):
    return students.get(student_id, "Student not found")



@app.post("/students/{student_id}")
def create_student(student_id: int, name: str, age: int):
    students[student_id] = {"name": name, "age": age}
    return {"message": "Student added successfully"}


@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int):
    students[student_id] = {"name": name, "age": age}
    return {"message": "Student updated successfully"}


@app.patch("/students/{student_id}")
def patch_student(student_id: int, age: int):
    if student_id in students:
        students[student_id]["age"] = age
        return {"message": "Age updated successfully"}
    return {"message": "Student not found"}



@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id in students:
        del students[student_id]
        return {"message": "Student deleted successfully"}
    return {"message": "Student not found"}



#-----------------
#      Task
#-----------------




class TaskCreate(BaseModel):
    title: str
    done: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    done: bool


tasks = {}
next_id = 1


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    global next_id
    task_data = {          
        "id": next_id,
        "title": task.title,
        "done": task.done
    }
    tasks[next_id] = task_data
    next_id += 1
    return task_data


@app.get("/tasks")
def get_tasks():
    return {"tasks": list(tasks.values())}


@app.get("/tasks/{id}")
def get_task(id: int):
    if id not in tasks:
        raise HTTPException(
            status_code=404,
            detail=f"Task with id {id} not found."
        )
    return tasks[id]


@app.put("/tasks/{id}")
def update_task(id: int, task: TaskCreate):   
    if id not in tasks:
        raise HTTPException(
            status_code=404,
            detail=f"Task with id {id} not found."
        )
    tasks[id]["title"] = task.title
    tasks[id]["done"] = task.done
    return tasks[id]


@app.delete("/tasks/{id}")
def delete_task(id: int):
    if id not in tasks:
        raise HTTPException(
            status_code=404,
            detail=f"Task with id {id} not found."
        )
    deleted = tasks.pop(id)
    return {"message": f"Task '{deleted['title']}' deleted successfully."}