from fastapi import FastAPI
from databases import Database
from models import User


DATABASE_URL = "postgresql://dae22:1998@localhost/mydatabase"
database = Database(DATABASE_URL)

async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

@app.post("/registration")
async def registration(user: User):
    query = "INSERT INTO users (username, email, password) VALUES (:username, :email, :password)"
    values = user.model_dump()
    await database.execute(query, values)
    return {"message": "Регистрация прошла успешно"}

@app.get("/users")
async def get_users():
    query = "SELECT username FROM users"
    rows = await database.fetch_all(query)
    return {"Users": rows}

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    query = "DELETE FROM users WHERE id=:user_id RETURNING id"
    values = {"user_id": user_id}
    result = await database.execute(query, values)
    return {"message": f"Пользователь {result} удален"}