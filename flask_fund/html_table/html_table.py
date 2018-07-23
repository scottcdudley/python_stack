from flask import Flask, render_template, request, redirect, session
app = Flask(name)

app.secret_key = 'word'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
return render_template("NinjaGold.html", count = session['count'])
@app.route('/get_gold')
def inc():
        session['count'] += random.randint(10,20)
        return redirect('/')
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
if name=="main":
    app.run(debug=True)
