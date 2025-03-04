from fastapi import FastAPI, Cookie, Response, HTTPException
from uuid import uuid1
from models.models import User


app = FastAPI()

fake_db: list[User] = [User(username='user123', password='password123'),
                       User(username="dae22", password="yanedyrak"),
                       User(username="Noigu", password="hoyopo")]
sessions: dict = {}


@app.get('/login')
async def login(user: User, response: Response):
    for person in fake_db:
        if person.username == user.username and person.password == user.password:
            return {"message": "You got my secret, welcome"}
        raise HTTPException(status_code=401)





