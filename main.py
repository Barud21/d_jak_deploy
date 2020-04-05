from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

app.counter = 0
app.patients = []

##############################################################
# Zadanie 1
##############################################################

@app.get('/')
def hello_world():
    return {"message": "Hello World during the coronavirus pandemic!"}


##############################################################
# Zadanie 2
##############################################################

@app.get('/method')
def return_get():
    return {"method": "GET"}

@app.post('/method')
def return_post():
    return {"method": "POST"}

@app.put('/method')
def return_put():
    return {"method": "PUT"}

@app.delete('/method')
def return_delete():
    return {"method": "DELETE"}


##############################################################
# Zadanie 3
##############################################################

class patient_data_rq(BaseModel):
    name: str
    surename: str


class patient_data_resp(BaseModel):
    id: int
    patient: patient_data_rq

# #TODO: zrobić licznik przechowujący liczbę wejść na stronę

@app.post('/patient')
def patient_data(rq: patient_data_rq):
    app.patients.append(rq)
    app.counter += 1
    return patient_data_resp

##############################################################
# Zadanie 4
##############################################################








##############################################################
##############################################################

# class HelloNameResp(BaseModel):
#     message: str
#
# @app.get('/hello/{name}', response_model=HelloNameResp)
# def hello_name(name: str):
#     return HelloNameResp(message=f"Hello {name}")
#
#
# class GiveMeSomethingRq(BaseModel):
#     first_key: str
#
#
# class GiveMeSomethingResp(BaseModel):
#     received: Dict
#     constant_data: str = "python jest super"
#
#
# @app.post("/dej/mi/coś", response_model=GiveMeSomethingResp)
# def receive_something(rq: GiveMeSomethingRq):
#     return GiveMeSomethingResp(received=rq.dict())
