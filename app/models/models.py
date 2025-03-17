from pydantic import BaseModel, UUID4
from typing import Optional


class Todo(BaseModel):
    title: str
    description: str
    completed: str = 'false'

from pydantic import BaseModel
import uuid

class User(BaseModel):
    username: str
    password: str
