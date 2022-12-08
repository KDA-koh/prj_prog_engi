from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    text: str

app = FastAPI()
classifier = pipeline("text2text-generation",
                      model="czearing/story-to-title")


@app.get("/")
def root():
    return {"message": "texttext"}


@app.post("/title/")
def predict(item: Item):
    output = classifier(item.text)
    return {"I suggest for your text this title": output}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='localhost')
