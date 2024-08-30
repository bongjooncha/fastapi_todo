from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from todo import todo_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 앱의 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to the FastAPI"}

app.include_router(todo_router)
