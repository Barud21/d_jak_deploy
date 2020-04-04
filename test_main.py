from fastapi.testclient import TestClient
from main import app
import pytest
#import pytest

client = TestClient(app)

def test_hello_world():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World during the coronavirus pandemic!"}



##############################################################
# Zadanie 3
##############################################################

#@pytest.mark.parametrize("id, name, surename", [(0, "Bartek", "Rudzinski"), (1, "Brad", "Pitt"), (2, "Kamui", "Kobayashi")])
def test_patient_data():
    response = client.post('/patient', json={"name": "Bartek", "surename": "Rudzinski"})
    assert response.status_code == 200
    assert response.json() == {"id": 0, "patient": {"name": "Bartek", "surename": "Rudzinski"}}


##############################################################
# Zadanie 4
##############################################################


@pytest.mark.parametrize("name", ["Ala", "Zażółć Gęślą jaźń", "Grzegorz Brzęczyszczykiewicz"])
def test_hello_name(name):
    response = client.get(f'/hello/{name}')
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {name}"}

def test_receive_something():
    response = client.post("/dej/mi/coś", json={'first_key': 'some_value'})
    assert response.json() == {"received": {'first_key': 'some_value'},
                               "constant_data": "python jest super"}

# def test_return_method():
#     response = client.get('/method')
#     assert response.status_code == 200
#     assert response.json() == {"message": "METHOD"}
