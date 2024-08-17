import os
import pytest
from fastapi.testclient import TestClient
from main.settings import app, REDIS_CONNECT


# Убедитесь, что Redis пуст перед каждым тестом
@pytest.fixture(autouse=True)
def clear_redis():
    REDIS_CONNECT.flushdb()  # Очистка базы данных Redis перед каждым тестом
    yield
    REDIS_CONNECT.flushdb()  # Очистка базы данных Redis после каждого теста


client = TestClient(app)


def test_write_data():
    response = client.post("http://localhost:8000/write_data", json={"phone": "+79090000000", "address": "текстовый адрес"})
    assert response.status_code == 200
    assert response.json() == {"message": "Data saved successfully"}


def test_check_data():
    # Сначала запишем данные
    response = client.post("http://localhost:8000/write_data", json={"phone": "+79090000000", "address": "текстовый адрес"})
    assert response.status_code == 200  # Проверка, что данные успешно сохранены

    # Теперь проверим данные
    response = client.get("http://localhost:8000/check_data?phone=+79090000000")
    assert response.status_code == 200
    assert response.json() == {"phone": "+79090000000", "address": "текстовый адрес"}


def test_check_data_not_found():
    response = client.get("http://localhost:8000/check_data?phone=+79090000001")
    assert response.status_code == 404
    assert response.json() == {"detail": "Phone number not found"}
