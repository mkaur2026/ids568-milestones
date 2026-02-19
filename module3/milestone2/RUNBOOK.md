# RUNBOOK — Milestone 2 Service

## 1. Service Description

This project is a containerized FastAPI microservice with:

- GET /healthz → health check endpoint
- POST /predict → prediction endpoint (doubles input number)

---

## 2. Dependency Pinning Strategy

All dependencies are pinned in requirements.txt using exact versions (example: fastapi==0.110.0).

Pinning ensures:
- Reproducible builds
- No unexpected dependency updates
- Deterministic Docker image creation

Dependencies are installed in the builder stage of the multi-stage Dockerfile.

---

## 3. Image Optimization

This project uses a multi-stage Docker build to reduce image size and improve security.

### Optimization Techniques

- Separate **builder stage** for installing dependencies
- Minimal runtime stage using `python:3.11-slim`
- Only required application files copied into runtime image
- `.dockerignore` excludes unnecessary files
- Container runs as a non-root user (`appuser`)
- No build tools included in final image

### Image Size Measurement

Image size measured using:

docker images milestone2-service:local

Without multi-stage optimization (single-stage build with full Python image), image size would typically exceed 400–500MB.
Optimized multi-stage image size:

169 MB

This demonstrates significant reduction in size and attack surface.

---

## 4. Security Considerations

- No hardcoded credentials in repository
- Registry authentication handled via GitHub Secrets
- Minimal slim base image
- Multi-stage build removes build tools from runtime image
- Non-root container user (appuser)

---

## 5. CI/CD Workflow

GitHub Actions workflow performs:

1. Runs pytest
2. Builds Docker image
3. Authenticates to Artifact Registry
4. Pushes image only if tests pass
5. Tags image using semantic versioning

Pipeline triggers:
- On push to main
- On semantic version tags (vX.Y.Z)

---

## 6. Versioning Strategy

Semantic versioning is used:

vMAJOR.MINOR.PATCH

Examples:
- v1.0.0
- v1.0.1

Final submission tag:

m2-submission

---

## 7. Troubleshooting

### ModuleNotFoundError: app
Run pytest from inside module3/milestone2 directory.

### Docker daemon not running
Start Docker Desktop.

### Port already in use
Check containers:
docker ps

Stop container:
docker stop <container_id>

### Authentication error when pushing image
Verify GitHub Secrets configuration.


