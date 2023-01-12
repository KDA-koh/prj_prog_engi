from transformers import pipeline
from flask import Flask,render_template,request

app = Flask(__name__)
classifier = pipeline("text2text-generation", model="czearing/story-to-title")

@app.route("/")
def hello_world():
    return render_template('main_page.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = classifier(text)[0]
    return render_template('main_page.html', text = processed_text.get('generated_text'))

if __name__ == '__main__':
    app.run()
