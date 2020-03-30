from fastapi.testclient import TestClient
from w01_z01 import app
import pytest


client = TestClient(app)

def test_hello_corona():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello World during the coronavirus pandemic!"}

