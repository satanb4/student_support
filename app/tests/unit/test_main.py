import httpx
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_response():
    response = client.get("/")
    assert response.status_code == 200
