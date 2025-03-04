from pydantic import BaseModel
import uuid

class User(BaseModel):
    username: str
    password: str


