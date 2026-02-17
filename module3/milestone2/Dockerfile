# Stage 1: Builder (installs Python deps)
FROM python:3.11-slim AS builder

WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


# Stage 2: Runtime (minimal image)
FROM python:3.11-slim

WORKDIR /app

# Create non-root user
RUN useradd --create-home appuser
USER appuser

# Copy installed deps from builder into runtime user's home
COPY --from=builder /root/.local /home/appuser/.local

# Copy application code
COPY --chown=appuser:appuser app/ ./app
COPY --chown=appuser:appuser tests/ ./tests

# Ensure user-installed binaries are on PATH
ENV PATH="/home/appuser/.local/bin:$PATH"

# Expose port (FastAPI default we'll use is 8000)
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

