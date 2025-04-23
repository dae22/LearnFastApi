from fastapi.testclient import TestClient
from app.main import app
import pytest


@pytest.fixture
def client():
    return TestClient(app)

def test_calculate_sum(client):
    # Тест 1: валидные входные данные
    response = client.get("/sum/", params={"a": 5, "b": 10})
    assert response.status_code == 200
    assert response.json() == {"result": 15}

    # Тест 2: отрицательные числа
    response = client.get("/sum/", params={"a": -8, "b": -3})
    assert response.status_code == 200
    assert response.json() == {"result": -11}

    # Тест 3: ноль и положительное число
    response = client.get("/sum/", params={"a": 0, "b": 7})
    assert response.status_code == 200
    assert response.json() == {"result": 7}

    # Тест 4: одно число не введено
    response = client.get("/sum/", params={"a": 3})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["query", "b"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }