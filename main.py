from transformers import pipeline
from flask import Flask,render_template,request

web_app = Flask(__name__)
classifier = pipeline("text2text-generation", model="czearing/story-to-title")

@web_app.route("/")
def hello_world():
    return render_template('main_page.html')

@web_app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = classifier(text)[0]
    return render_template('main_page.html', text = processed_text.get('generated_text'))

if __name__ == '__main__':
    web_app.run()
