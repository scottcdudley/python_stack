from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'ThisisSecret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result')
def results():
    return render_template("result.html")

@app.route('/process',methods=['POST'])
def process():
    count = 0
    if len(request.form['first_name']) < 2:
        flash("invalid length.  name should be larger than 2 characters")
        count+=1
    if len(request.form['last_name']) < 1:
        flash("Last name cannot be blank!")
        count+=1
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        count+=1
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters!")
        count+=1
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        count+=1
    if request.form['password'] != request.form['password_confirm']:
        flash("Passwords do not match!")
        count+=1
    if count >  0:
        return redirect('/')
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    flash("Thanks for submitting your information")    
    return redirect('/')

app.run(debug=True)