from flask import Flask, url_for, render_template, jsonify
import time
import random
app = Flask(__name__)


@app.route('/home')
def hello_world():
    return render_template('index.html')

@app.route('/home/<gebruiker>')
def groet(gebruiker):
    return render_template('index.html', gebruiker=gebruiker)
    
@app.route('/api/deelnemers/<int:max_age>', methods=['GET'])
def deelnemerlijst(max_age):
    result = []
    for i in range(5):
        result.append({'type':'persoon', 'leeftijd':random.randint(0,max_age)})
    return jsonify(result)