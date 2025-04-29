from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=16)
