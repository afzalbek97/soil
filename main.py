from fastapi import FastAPI, HTTPException, Path, Query
"""FastAPI uses Starlette Framework under the hood"""
from fastapi import Request
from provider import Student, students

print("\n Backend Server Is Running \n")
app = FastAPI(title="Landing FastAPI soil")


@app.get("/")
async def get_greeting(request: Request) -> str:
    print("request:", request)
    return "Hello from Starlette"


@app.get("/message", response_model=dict)
async def get_message():
    return {"message": "Hi, MIT"}


# FastAPI handles JESON
@app.get("/mit/all", response_model=dict[int, Student]) 
def get_students():
    return students


# Path params
@app.get("/mit/student/{id}", response_model=Student)
def get_students_by_id(id: int = Path (ge=1)):
    if id not in students:
        raise HTTPException(
            status_code=400, detail=f"Student id={id} not found!"
            )
    return students[id]


# Query params
@app.get("/mit/student", response_model=list[Student])
def get_student_by_name(name: str = Query(min_length=3, max_length=20)):
    result = [s for s in students.values() if s.name == name]
    return result


@app.post("/mit/edit/{id}", response_model=Student)
def edit_student(
    id: int = Path(ge=1),
    name: str = Query(min_length=3, max_length=20),
    age: int = Query(gt=20)
):
    print(f"the path: {id=} and query: {name=}, {age=}")
    
    if id not in students:
        raise HTTPException(
            status_code=400, detail=f"Student {id=} not found!")
        
    student = students[id]
    student.name = name
    student.age = age
    return student

