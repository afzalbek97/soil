from fastapi import FastAPI
"""FastAPI uses Starlette Framework under the hood"""
from starlette.requests import Request, Response


print("\n Backend Server Is Running \n")
app = FastAPI(title="Landing FastAPI soil")


@app.get("/")
async def get_greeting(request: Request, response: Response):
    print("request:", request)
    response.status_code = 200
    response.body = b"Hello from Starlette"
    print("response:", response)
    return response