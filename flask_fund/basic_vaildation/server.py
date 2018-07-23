from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
    if len(request.form['name']) < 1:
        flash("Name connot be empty!")
    else:
        flash(f"Success! You name is {request.form['name']}.")
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)