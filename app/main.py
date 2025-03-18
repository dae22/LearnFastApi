from fastapi import FastAPI, HTTPException
from databases import Database
from models.models import UserCreate, UserReturn

app = FastAPI()

DATABASE_URL = "postgresql://dae22:1998@localhost/mydatabase"

database = Database(DATABASE_URL)


@app.on_event("startup")
async def startup_database():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_database():
    await database.disconnect()


@app.post("/users/", response_model=UserReturn)
async def create_user(user: UserCreate):
    query = "INSERT INTO users (username, email) VALUES (:username, :email) RETURNING id"
    values = {"username": user.username, "email": user.email}
    try:
        user_id = await database.execute(query=query, values=values)
        return {**user.dict(), "id": user_id}
    except:
        raise HTTPException(status_code=500, detail="Failed to create user")

@app.get("/users/{user_id}", response_model=UserReturn)
async def get_user(user_id: int):
    query = "SELECT * FROM users WHERE id=:user_id"
    values = {"user_id": user_id}
    try:
        result = await database.fetch_one(query=query, values=values)
    except:
        raise HTTPException(status_code=500, detail="Failed to get user from database")
    if result:
        return UserReturn(username=result["username"], email=result["email"], id=user_id)
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=UserReturn)
async def update_user(user_id: int, user:UserCreate):
    query = "UPDATE users SET username=:username, email=:email WHERE id=:id"
    values = {"username": user.username, "email": user.email, "id": user_id}
    try:
        await database.execute(query=query, values=values)
        return {**user.dict(), "id": user_id}
    except:
        raise HTTPException(status_code=500, detail="Failed to update user in database")

@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    query = "DELETE FROM users WHERE id=:id RETURNING id"
    values = {"id": user_id}
    try:
        deleted_rows = await database.execute(query=query, values=values)
    except:
        raise HTTPException(status_code=500, detail="Failed to delete user from database")
    if deleted_rows:
        return {"message": " User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
