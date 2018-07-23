from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)

mysql = connectToMySQL('lead_gen_business')
app.secret_key="rAdiOhEad"

@app.route('/')
def index():
    if 'start_date' in session:
        query = "SELECT CONCAT(clients.first_name, ' ', clients.last_name) as 'client', COUNT(clients.client_id) FROM clients JOIN sites ON clients.client_id = sites.client_id JOIN leads ON sites.site_id = leads.site_id WHERE registered_datetime > %(start_date)s AND registered_datetime < %(end_date)s GROUP BY clients.client_id"
        data = {
            'start_date': session['start_date'],
            'end_date': session['end_date']
        }
        search = mysql.query_db(query, data)
    else:
        query = "SELECT CONCAT(clients.first_name, ' ', clients.last_name) as 'client', COUNT(clients.client_id) FROM clients JOIN sites ON clients.client_id = sites.client_id JOIN leads ON sites.site_id = leads.site_id WHERE registered_datetime > '0000-00-00 00:00:00' AND registered_datetime < '9999-12-31 23:59:59' GROUP BY clients.client_id"
        search = mysql.query_db(query)
    return render_template('index.html', data = search)

@app.route('/new_date', methods=['POST'])
def search():
    session['start_date'] = request.form['start']
    session['end_date'] = request.form['end']
    return redirect ('/')

if __name__ == "__main__":
  app.run(debug=True)