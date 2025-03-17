from models.models import Todo
import sqlite3
from database import get_db_connection
from fastapi import FastAPI


app = FastAPI()


@app.post("/todos")
def create_item(todo: Todo):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (title, description, completed) VALUES ($1, $2, $3)", (todo.title, todo.description, todo.completed))
    last_id = cursor.lastrowid
    row = cursor.execute("SELECT * FROM items WHERE id=?", (last_id,))
    conn.commit()
    conn.close()
    return row

@app.get("/todos/{todo_id}")
def read_item(todo_id: int):
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM items WHERE id=$1", todo_id)
    conn.close()
    return row

@app.put("/{id}")
def update_item(todo_id: int, todo: Todo):
    conn = get_db_connection()
    conn.execute("UPDATE items SET $2, $3, $4 WHERE id=$1", (todo_id, todo.title, todo.description, todo.completed))
    row = conn.execute("SELECT * FROM items WHERE id=$1", (todo_id,))
    conn.close()
    return row

@app.delete("/todos/{todo_id}")
def delete_item(todo_id: int):
    conn = get_db_connection()
    conn.execute("DELETE items WHERE id=$1", (todo_id,))
    return {"message": "Item deleted"}






