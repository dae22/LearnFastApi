from fastapi import FastAPI, HTTPException
from databases import Database
from models.models import Todo

app = FastAPI()

DATABASE_URL = "postgresql://dae22:1998@localhost/mydatabase"

database = Database(DATABASE_URL)


@app.on_event("startup")
async def startup_database():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_database():
    await database.disconnect()


@app.post("/todos")
async def create_item(todo: Todo):
    query = "INSERT INTO items (title, description, completed) VALUES (:title, :description, :completed) RETURNING id"
    values = todo.dict()
    try:
        user_id = await database.execute(query=query, values=values)
        return {**todo.dict(), "id": user_id}
    except:
        raise HTTPException(status_code=500, detail="Failed to create todo")

@app.get("/todos/{todo_id}")
async def get_item(todo_id: int):
    query = "SELECT * FROM items WHERE id=:todo_id"
    values = {"todo_id": todo_id}
    try:
        result = await database.fetch_one(query=query, values=values)
    except:
        raise HTTPException(status_code=500, detail="Failed to get todo from database")
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}")
async def update_user(todo_id: int, todo: Todo):
    query = "UPDATE items SET title=:title, description=:description, completed=:completed WHERE id=:id"
    values = {"title": todo.title, "description": todo.description, "completed": todo.completed, "id": todo_id}
    try:
        await database.execute(query=query, values=values)
        return {**todo.dict(), "id": todo_id}
    except:
        raise HTTPException(status_code=500, detail="Failed to update todo in database")

@app.delete("/todos/{todo_id}", response_model=dict)
async def delete_user(todo_id: int):
    query = "DELETE FROM items WHERE id=:id RETURNING id"
    values = {"id": todo_id}
    try:
        deleted_rows = await database.execute(query=query, values=values)
    except:
        raise HTTPException(status_code=500, detail="Failed to delete todo from database")
    if deleted_rows:
        return {"message": " Todo deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Todo not found")
