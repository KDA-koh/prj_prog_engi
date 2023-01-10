from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from transformers import pipeline
from pydantic import BaseModel
import uvicorn
from flask import Flask,render_template,request


class Item(BaseModel):
    text: str

#app = FastAPI()
web_app = Flask(__name__)
#classifier = pipeline("text2text-generation", model="czearing/story-to-title")

@web_app.route("/")
def hello_world():
    return render_template('main_page.html')

@web_app.route('/', methods=['POST'])
#def my_form_post():
#    text = request.form['text']
#    processed_text = text.upper()
#    return render_template('main_page.html', text = processed_text)
def predict(item: Item):
    #output = classifier(item.text)
    #return {"I suggest for your text this title": output}
    return '<h1>hi, my name is...</h1>'



@web_app.route("/", methods=['POST'])
def predict(item: Item):
    #output = classifier(item.text)
    #return {"I suggest for your text this title": output}
    return 'hi, my name is...'



if __name__ == '__main__':
    web_app.run()
