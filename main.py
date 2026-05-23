from fastapi import FastAPI
"""FastAPI uses Starlette Framework under the hood"""
from fastapi import Request


print("\n Backend Server Is Running \n")
app = FastAPI(title="Landing FastAPI soil")


@app.get("/")
async def get_greeting(request: Request) -> str:
    print("request:", request)
    return "Hello from Starlette"

@app.get("/message", response_model=dict)
async def get_message():
    return {"message": "Hi Afzal"}