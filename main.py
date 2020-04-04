from dataclasses import dataclass
from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def hello_world():
    return {"message": "Hello World during the coronavirus pandemic!"}

##############################################################
# Zadanie 2
##############################################################

# @app.get('/method')
# def return_method_name():
#
#     return {"method": "METHOD"}

##############################################################
# Zadanie 3
##############################################################

class patient_data_rq(BaseModel):
    name: str
    surename: str


class patient_data_resp(BaseModel):
    id: int = 0
    patient: Dict

#TODO: zrobić licznik przechowujący liczbę wejść na stronę

@app.post('/patient')
def patient_data(rq: patient_data_rq):
    return patient_data_resp(patient=rq.dict())

##############################################################
# Zadanie 4
##############################################################




##############################################################
##############################################################


class HelloNameResp(BaseModel):
    message: str

@app.get('/hello/{name}', response_model=HelloNameResp)
def hello_name(name: str):
    return HelloNameResp(message=f"Hello {name}")


class GiveMeSomethingRq(BaseModel):
    first_key: str


class GiveMeSomethingResp(BaseModel):
    received: Dict
    constant_data: str = "python jest super"


@app.post("/dej/mi/coś", response_model=GiveMeSomethingResp)
def receive_something(rq: GiveMeSomethingRq):
    return GiveMeSomethingResp(received=rq.dict())
