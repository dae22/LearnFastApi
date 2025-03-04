from fastapi import FastAPI, HTTPException, Depends
from models.models import User
from fastapi.security import HTTPBasic, HTTPBasicCredentials


app = FastAPI()
security = HTTPBasic()


fake_db: list[User] = [User(username='user123', password='password123'),
                       User(username="dae22", password="Boston")]


def auth(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status_code=401, detail="You pick the wrong house, Fool", headers={"WWW-Authenticate": "Basic"})
    return user

def get_user(username: str):
    for user in fake_db:
        if user.username == username:
            return user
    return None


@app.get('/login')
def login(user: User = Depends(auth)):
    return {"message": "You got my secret, welcome"}





