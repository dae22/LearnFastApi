from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str
    completed: str = 'false'

