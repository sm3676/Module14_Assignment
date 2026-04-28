from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

def test_register():
    email = f"{uuid.uuid4()}@test.com"

    response = client.post("/users/register", json={
        "email": email,
        "password": "123456"
    })

    assert response.status_code == 200


def test_login():
    email = f"{uuid.uuid4()}@test.com"

    # 👉 first register user
    client.post("/users/register", json={
        "email": email,
        "password": "123456"
    })

    # 👉 then login
    response = client.post("/users/login", json={
        "email": email,
        "password": "123456"
    })
    assert response.status_code == 200