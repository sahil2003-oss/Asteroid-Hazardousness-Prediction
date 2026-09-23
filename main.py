from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel, Field
import joblib
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)
input_features = [
    "Minimum_Orbit_Intersection",
    "Absolute_Magnitude",
    "Maximum_Possible_Estimated_Diameter",
]

model = joblib.load("asteroid_hazard_model.pkl")


# Pydantic Model: Responsible for performing Input Data Validaiton
class Features(BaseModel):
    Minimum_Orbit_Intersection: float = Field(...)
    Absolute_Magnitude: float = Field(..., ge=11.16, le=32.1)
    Maximum_Possible_Estimated_Diameter: float = Field(..., ge=0, le=35)


@app.get("/")
def greet():
    return "hello guys!"


@app.post("/make_prediction")
def predict(data: Features):
    input_row = pd.DataFrame([dict(data)], columns=input_features)
    prediction = model.predict(input_row)
    probablity = model.predict_proba(input_row)
    if int(prediction[0]) == 0:
        hazardousness = "Non-Hazardous"
    else:
        hazardousness = "Hazardous"
    return {
        "IS ASTEROID HAZARDOUS": hazardousness,
        "PROBABLITY": probablity.tolist(),
    }
