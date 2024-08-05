import random

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title='Jenkins CI/CD Test',
    description='A simple CI/CD app',
    version='1.0'
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def index():
    return {"message": "simple jenkins app using ml"}


class Arg1(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Self_Employed: str


def generate_prediction(data_input):
    print(data_input)
    return random.randint


@app.post("/status")
def predict(arg1: Arg1):
    data = arg1.model_dump()
    prediction = generate_prediction([data])
    if prediction == "9":
        return "YES"
    else:
        return "NO"


@app.post("/status_ui")
def predict_ui(Gender: str,
               Married: str,
               Dependents: str,
               Self_Employed: str):
    input_data = [Gender, Married, Dependents, Self_Employed]

    cols = ['Gender', 'Married', 'Dependents', 'Self_Employed']

    data_dict = dict(zip(cols, input_data))
    prediction = generate_prediction([data_dict])
    if prediction == "9":
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)
