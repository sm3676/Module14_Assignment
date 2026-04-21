from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crud():
    # Create
    res = client.post("/calculations/", json={
        "expression": "2+2",
        "result": "4"
    })
    assert res.status_code == 200
    data = res.json()
    calc_id = data["id"]

    # Read
    res = client.get(f"/calculations/{calc_id}")
    assert res.status_code == 200

    # Update
    res = client.put(f"/calculations/{calc_id}", json={
        "expression": "3+3",
        "result": "6"
    })
    assert res.status_code == 200

    # Delete
    res = client.delete(f"/calculations/{calc_id}")
    assert res.status_code == 200