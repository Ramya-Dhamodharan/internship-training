from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my first FastAPI app!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}! Welcome to FastAPI."}

@app.get("/Hello/{name}/{Password}")
def test(name:str, password=1234):
    return{"message:"f"Hello {name}."}


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
