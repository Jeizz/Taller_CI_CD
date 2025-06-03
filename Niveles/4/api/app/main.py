from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, generate_latest
from starlette.responses import Response
import pickle
import os

app = FastAPI()
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

PREDICTION_COUNTER = Counter("predictions_total", "Número total de predicciones")

class InputData(BaseModel):
    x: float

@app.post("/predict")
def predict(data: InputData):
    PREDICTION_COUNTER.inc()
    result = model.predict([[data.x]])[0]
    return {"prediction": result}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

@app.get("/version")
def get_version():
    return {"version": "v1.0.0"} 

