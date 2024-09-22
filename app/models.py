# app/models.py
from pydantic import BaseModel
from typing import Optional

# Task model using Pydantic
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
