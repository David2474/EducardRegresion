from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from app.utils import contar_respuestas, generar_grafica
import numpy as np
import os

class InputData(BaseModel):
    answers: list[int]

app = FastAPI()

model_path = "model/modelo_bosque.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Modelo no encontrado en {model_path}")

model = joblib.load(model_path)

@app.post("/")
def predict(data: InputData):
    prediction = model.predict([data.answers])[0]
    probs = model.predict_proba([data.answers])[0]
    labels = model.classes_

    probabilidades = {
        labels[i]: round(probs[i] * 100, 2)
        for i in range(len(labels))
    }

    conteo = contar_respuestas(data.answers)
    grafica_path = generar_grafica(data.answers)

    return {
        "prediction": prediction,
        "probabilidades": probabilidades,
        "conteo": {
            "visual": conteo[0],
            "auditivo": conteo[1],
            "kinestesico": conteo[2]
        },
        "grafica_path": grafica_path
    }
