from main import app
from fastapi.testclient import TestClient

client = app.test_client()

"""
def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': "texttext"}


def test_predict_dog():
    response = client.post("/title/", json={"text": "A young orphan girl adopts a dog, completely unaware that its supposedly a dangerous scientific experiment thats taken refuge on Earth and is now hiding from its creator"})
    if response.status_code == 200:
        json_data = response.json()
        assert json_data[0] == {'generated_text': 'Dog'}
"""

def test_request_example(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': "texttext"}
