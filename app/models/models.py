from pydantic import BaseModel, UUID4
from typing import Optional


class Todo(BaseModel):
    title: str
    description: str
    completed: str = 'false'
