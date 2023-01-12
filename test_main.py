import pytest
from main import app


@pytest.fixture()
def client():
    return app.test_client()


"""
def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': "texttext"}
"""




def test_request_example(client):
    response = client.get("/")
    assert response.status_code == 200

def test_predict_dog(client):
    response = client.post("/", json={"text": "A young orphan girl adopts a dog, completely unaware that its supposedly a dangerous scientific experiment thats taken refuge on Earth and is now hiding from its creator"})
    assert response.json['generated_text'] == 'Dog'