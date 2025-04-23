from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class User(BaseModel):
    username: str
    age: int = Field(gt=18)
    email: EmailStr
    password: str = Field(min_length=8, max_length=16)
    phone: Optional[str] = 'Unknown'
