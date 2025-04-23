from fastapi import FastAPI
from databases import Database

app = FastAPI()

DATABASE_URL = "postgresql://dae22:1998@localhost/mydatabase"

database = Database(DATABASE_URL)


@app.get("/sum")
def calculate_sum(a: int, b: int):
    return {"result": a + b}
