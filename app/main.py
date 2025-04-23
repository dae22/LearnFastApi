from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from databases import Database
from models.models import *

app = FastAPI()

DATABASE_URL = "postgresql://dae22:1998@localhost/mydatabase"

database = Database(DATABASE_URL)


@app.get("/sum")
def calculate_sum(a: int, b: int):
    return {"result": a + b}
