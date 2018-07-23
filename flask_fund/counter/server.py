from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'chickensandmonkeysandturtles'

@app.route('/')
def index():
    if 'visits' not in session:
        session['visits'] = 0
    else:
        session['visits'] += 1
    return render_template('index.html',session=session)

@app.route('/test')
def test_route():
    user_details = {
        'name': 'Scott',
        'email': 'scott.dudley@sd.com'
    }

    return render_template('test.html', user=user_details)

@app.route('/create_or_destroy', methods=['POST'])
def process():
    if request.form['action'] == 'add':
        session['visits'] += 1
        return redirect("/")
    if request.form['action'] == 'reset':
        del session['visits']
        return redirect("/")

if __name__ == "__main__":
  app.run(debug=True)
