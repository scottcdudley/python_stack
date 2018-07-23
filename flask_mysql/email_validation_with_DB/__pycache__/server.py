from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'PiNkFl0yD'

from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app, 'email_validation_db')

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
	email_address = request.form['email']
	session['email'] = email_address

	if EMAIL_REGEX.match(session['email']):
		session['valid'] = True
		flash("The email address(" + email_address + ") is Valid)

		query = "SELECT * FROM email_addresses WHERE email_address = :email"
		data = {'email': email_address}
		user = mysql.query_db(query, data)

		if len(user) == 0:
			query = "INSERT INTO email_addresses (email_address, created_at, updated_at) VALUES (:email, NOW(), NOW())"
			data = {'email': email_address}
			mysql.query_db(query, data)
		return redirect('/success')
	else:
		flash("That is not a valid email")
		return redirect('/')

@app.route('/success')
def success():
	if session['valid'] == True:
		query = "SELECT id, email_address as email, created_at as date FROM email_addresses"
		email_list = mysql.query_db(query)
		return render_template('success.html', addresses=email_list)
	else:
		return redirect('/')

@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')

@app.route('/delete/<id>')
def delete(id):
	query = 'DELETE FROM email_addresses WHERE id=:id'
	data = {'id': id}

	mysql.query_db(query, data)
	flash('Email deleted.', 'error')

	return redirect('/success')


app.run(debug=True)