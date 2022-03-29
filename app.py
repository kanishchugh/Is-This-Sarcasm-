from crypt import methods
from urllib import request
from flask import Flask, render_template, request
from sarcasm import Sarcasm
app = Flask(__name__)

@app.route('/')
def index():
    # text = request.form['Search']
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    text = request.form['text']
    sarcasm = Sarcasm(path='./data/Sarcasm.json')
    a = sarcasm.run(text)
    
    if a == 'Not Sarcasm':
        location = '../static/Not_Sarcasm.gif'
        
    else:
        location = '../static/Sarcasm.gif'
    return render_template('result.html', location = location)
    
if __name__ == '__main__':
    app.run()