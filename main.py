from fastapi import FastAPI, HTTPException
"""FastAPI uses Starlette Framework under the hood"""
from fastapi import Request
from provider import students


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
@app.get("/mit/all", response_model=dict[int, dict]) 
def get_students():
    return students


# Path params
@app.get("/mit/student/{id}", response_model=dict)
def get_students_by_id(id: int):
    if id not in students:
        raise HTTPException(
            status_code=400, detail=f"Student id={id} not found"
            )
    return students[id]


# Query params
@app.get("/mit/student", response_model=list[dict])
def get_student_by_name(name: str):
    result = [s for s in students.values() if s["name"] == name]
    return result
