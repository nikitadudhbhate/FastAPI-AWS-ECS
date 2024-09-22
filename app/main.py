# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from .models import Task

app = FastAPI()

# In-memory storage for tasks (no database)
tasks = []

# Endpoint to add a new task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

# Endpoint to get all tasks
@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks

# Endpoint to update a task (mark as completed)
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Endpoint to delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
