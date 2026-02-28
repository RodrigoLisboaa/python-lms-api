import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_login_and_me():
    email = f"test-{uuid.uuid4()}@example.com"
    password = "strongpass123"

    r = client.post("/auth/register", json={"email": email, "password": password, "full_name": "Test User"})
    assert r.status_code == 201, r.text

    r = client.post("/auth/login", data={"username": email, "password": password})
    assert r.status_code == 200, r.text
    token = r.json()["access_token"]

    r = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200, r.text
    assert r.json()["email"] == email