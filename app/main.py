from fastapi import FastAPI
from pydantic import BaseModel
from models.models import Feedback


app = FastAPI()

fake_db = []

@app.post('/feedback')
def add_feedback(feedback: Feedback):
    fake_db.append(feedback)
    return {"message": "Feedback added"}