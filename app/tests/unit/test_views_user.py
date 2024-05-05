from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_graph_endpoint():
    response = client.get("/graph")
    assert response.status_code == 200
    assert response.__sizeof__() > 1
