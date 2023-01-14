import pytest
from main import app, predict


@pytest.fixture()
def client():
    return app.test_client()

def test_request_example(client):
    response = client.get("/")
    assert response.status_code == 200

def test_predict_dog(client):
    text= "A young orphan girl adopts a dog, completely unaware that its supposedly a dangerous scientific experiment thats taken refuge on Earth and is now hiding from its creator"
    assert predict(text) == 'Dog'

def test_predict_star_wars(client):
    text = "Amid a galactic civil war, Rebel Alliance spies have stolen plans to the Galactic Empire's Death Star, a massive space station capable of destroying entire planets. Imperial Senator Princess Leia Organa of Alderaan, secretly one of the Rebellion's leaders, has obtained its schematics, but her starship is intercepted by an Imperial Star Destroyer under the command of the ruthless Darth Vader. Before she is captured, Leia hides the plans in the memory system of astromech droid R2-D2, who flees in an escape pod to the nearby desert planet Tatooine alongside his companion, protocol droid C-3PO. "
    assert predict(text) == 'Star Wars Rebel Alliance'

def test_predict_none(client):
    text = ''
    assert predict(text) == ''

def test_predict_nums(client):
    text = '123'
    assert predict(text) == '123'
