import pytest
from fastapi.testclient import TestClient
from app.main import app, DATABASE_URL
from databases import Database

client = TestClient(app)

@pytest.mark.asyncio
@pytest.fixture(scope="session", autouse=True)
async def setup_database():
    db = Database(DATABASE_URL)
    await db.connect()
    await db.execute(
        """ CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        ) """
    )
    yield
    await db.execute("DROP TABLE IF EXISTS users;")
    await db.disconnect()


@pytest.mark.asyncio
async def test_registration(setup_database):
    user = {
        "username": "dae22",
        "email": "dae-22@mail.ru",
        "password": "durilka22"
    }
    response = client.post("/registration", json=user)
    assert response.status_code == 200
    assert response.json() == {"result": {"message": "Регистрация прошла успешно"}}
