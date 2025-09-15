from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Example resource model
tasks = []

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Task Manager!"}

# Add your CRUD endpoints here
# See assignment README for requirements
