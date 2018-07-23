from flask import Flask, render_template, session, request, flash, redirect
import random


app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def gold():
    if 'x' not in session:
        session ['x'] = 0
    
    if 'activity' not in session:
        session['activity'] = []
    
    return render_template('index.html',x =session['x'])

@app.route('/process_money', methods=['POST'])
def process_money():
    
    if request.form['building'] == 'farm':
        session['x']+=random.randint(10,21)
    elif request.form['building'] == 'cave':
        session['x']+=random.randint(5,11)
    elif request.form['building'] == 'house':
        session['x']+=random.randint(2,16)
    if session['x']<=0:
        return render_template('index.html',x ="you broke")
    elif request.form['building'] == 'casino':
        session['x']+=random.randint(-50,51)

   
    return redirect('/')

@app.route('/reset')
def rese():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)