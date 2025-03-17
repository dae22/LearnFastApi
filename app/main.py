from fastapi import FastAPI
from models.models import Todo
import sqlite3
from database import get_db_connection
from fastapi import FastAPI, Cookie, Response, HTTPException
from uuid import uuid1
from models.models import User


app = FastAPI()


@app.post("/todos")
def create_item(todo: Todo):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (title, description, completed) VALUES ($2, $3, $4)", todo.title, todo.description, todo.completed)
    conn.commit()
    conn.close()
    return {"message": "Item added successfully!"}

@app.get("/todos/{todo_id}")
def read_item(todo_id: int):
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM todo.todo WHERE id=$1", todo_id)
    conn.close()
    return row

@app.put("/{id}")
def update_item(todo_id: int, todo: Todo):
    conn = get_db_connection()
    conn.execute("UPDATE todo.todo SET $2, $3, $4 WHERE id=$1", todo_id, todo.title, todo.description, todo.completed )
    row = conn.execute("SELECT * FROM todo.todo WHERE id=$1", todo_id)
    conn.close()
    return row

@app.delete("/todos/{todo_id}")
def delete_item(todo_id: int):
    conn = get_db_connection()
    conn.execute("DELETE todo.todo WHERE id=$1", todo_id)
    return {"message": "Item deleted"}

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





