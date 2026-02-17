# RUNBOOK — Milestone 2 Service

## Service Description
FastAPI microservice with health and prediction endpoints.

---

## Health Check

curl http://localhost:8000/healthz

Expected:
{"status":"ok"}

---

## Prediction Test

curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{"number":5}'

Expected:
{"prediction":10}

---

## Common Issues

### 1. ModuleNotFoundError: app
Run pytest from inside milestone2 directory.

### 2. Docker daemon not running
Start Docker Desktop.

### 3. Port already in use
Kill existing container:
docker ps
docker stop <container_id>

---

## Redeploy

Rebuild image:

docker build -t milestone2-service:local .

Re-run container:

docker run -p 8000:8000 milestone2-service:local

