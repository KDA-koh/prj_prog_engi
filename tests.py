from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': "texttext"}


def test_predict_dog():
    response = client.post("/predict/",
                           json={"text": "A young orphan girl adopts a dog, completely unaware that its supposedly a dangerous scientific experiment thats taken refuge on Earth and is now hiding from its creator"})
    json_data = response.json()

    assert response.status_code == 200
    assert json_data['label'] == 'Dog'
