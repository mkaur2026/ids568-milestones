# Milestone 2 — FastAPI Service with Docker & CI/CD

## Overview
This project is a containerized FastAPI service with:
- Health check endpoint
- Prediction endpoint
- Unit tests (pytest)
- Multi-stage Docker build
- GitHub Actions workflow that builds/tests/pushes on tags

## CI Status
![Build](https://github.com/mkaur2026/ids568-milestones/actions/workflows/build.yml/badge.svg)

## Endpoints

### GET /healthz
Response:
```json
{"status":"ok"}
POST /predict
Request:
{"number":5}
Response:
{"prediction":10}
If number < 0 → returns 400.
Run Locally (no Docker)
cd module3/milestone2
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
Run Tests
cd module3/milestone2
pytest -v
Build + Run with Docker (local)
cd module3/milestone2
docker build -t milestone2-service:local .
docker run --rm -p 8000:8000 milestone2-service:local
Test:
curl http://localhost:8000/healthz
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"number":5}'
Pull + Run from Artifact Registry (course registry)
Image reference:
us-central1-docker.pkg.dev/milestone1-mlops/milestone1-repo/milestone2-service:<TAG>
Example:
docker pull us-central1-docker.pkg.dev/milestone1-mlops/milestone1-repo/milestone2-service:v1.0.1
docker run --rm -p 8000:8000 us-central1-docker.pkg.dev/milestone1-mlops/milestone1-repo/milestone2-service:v1.0.1
Versioning
Images are published using semantic version tags (vX.Y.Z).
Final submission tag: m2-submission.
