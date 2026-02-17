from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict_success():
    response = client.post("/predict", json={"number": 5})
    assert response.status_code == 200
    assert response.json() == {"prediction": 10}

def test_predict_negative():
    response = client.post("/predict", json={"number": -1})
    assert response.status_code == 400

