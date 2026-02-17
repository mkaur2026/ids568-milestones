from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PredictRequest(BaseModel):
    number: float

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/predict")
def predict(req: PredictRequest):
    # Simple "model" logic so we can test it
    if req.number < 0:
        raise HTTPException(status_code=400, detail="number must be >= 0")
    return {"prediction": req.number * 2}

