from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'ninjaGold'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.form['building'] == 'farm':
        pull = random.randint(10, 20)
        session['building'] = 'Farm'
    elif request.form['building'] == 'cave':
        pull = random.randint(5, 10)
        session['building'] = 'Cave'
    elif request.form['building'] == 'house':
        pull = random.randint(2, 5)
        session['building'] = 'House'
    elif request.form['building'] == 'casino':
        pull = random.randint(-50, 50)
        print(pull)
        if pull < 0:
            if abs(pull) > session['gold']:
                pull = session['gold']*(-1)
        session['building'] = 'Casino'
    time = datetime.now()
    session['gold'] += pull
    if session['gold'] < 0:
        session['gold'] = 0
    if pull >= 0:
        session['win'] = True
    else:
        session['win'] = False
    info = {
        'pull': abs(pull), 
        'building': session['building'], 
        'time': time.strftime("%Y/%m/%d %I:%M %p"),
        'win': session['win']
        }
    session['activities'].append(info)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)