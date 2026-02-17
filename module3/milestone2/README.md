# Milestone 2 — FastAPI Service with Docker & CI

## Overview
This milestone builds a containerized FastAPI service with:

- Health check endpoint
- Prediction endpoint
- Unit testing with pytest
- Docker multi-stage build
- GitHub Actions CI
- Docker image build on tag

---

## Endpoints

### GET /healthz
Returns service health status.

Response:
{
  "status": "ok"
}

---

### POST /predict
Request:
{
  "number": 5
}

Response:
{
  "prediction": 10
}

If number < 0 → returns 400 error.

---

## Run Locally

Create virtual environment:

python3.11 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run app:

uvicorn app.main:app --reload

---

## Run Tests

pytest -v

---

## Build Docker Image

docker build -t milestone2-service:local .

Run container:

docker run -p 8000:8000 milestone2-service:local

---

## CI/CD

GitHub Actions runs:
- pytest
- Docker build
- Docker push on tag (v1.0.0)

