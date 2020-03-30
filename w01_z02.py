from fastapi import FastAPI
import pytest
import requests

app = FastAPI

@app.get('/method')
def method_type():
    @TODO: write
    return {"message": "METHOD"}