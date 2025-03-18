from models.models import Todo
from database import get_db_connection
from fastapi import FastAPI


app = FastAPI()


@app.post("/todos")
def create_item(todo: Todo):
    conn, cursor = get_db_connection()
    cursor.execute("INSERT INTO items (title, description, completed) VALUES (?, ?, ?)", (todo.title, todo.description, todo.completed))
    last_id = cursor.lastrowid
    cursor.execute("SELECT * FROM items WHERE id=?", (last_id,))
    row = cursor.fetchone()
    conn.commit()
    conn.close()
    return row

@app.get("/todos/{todo_id}")
def read_item(todo_id: int):
    conn, cursor = get_db_connection()
    cursor.execute("SELECT * FROM items WHERE id=?", (todo_id,))
    row = cursor.fetchone()
    conn.close()
    return row

@app.put("/todos/{todo_id}")
def update_item(todo_id: int, todo: Todo):
    conn, cursor = get_db_connection()
    cursor.execute("UPDATE items SET title=?, description=?, completed=? WHERE id=?", (todo.title, todo.description, todo.completed, todo_id))
    conn.commit()
    cursor.execute("SELECT * FROM items WHERE id=?", (todo_id,))
    row = cursor.fetchone()
    conn.close()
    return row

@app.delete("/todos/{todo_id}")
def delete_item(todo_id: int):
    conn, cursor = get_db_connection()
    cursor.execute("DELETE FROM items WHERE id=?", (todo_id,))
    conn.commit()
    conn.close()
    return {"message": "Item deleted"}






