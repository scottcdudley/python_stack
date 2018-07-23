from flask import Flask, render_template,redirect,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print("Got more info")
    name= request.form['name']
    email= request.form['email']
    dojo= request.form['select1']
    language= request.form['select2']
    comment= request.form['text']
    return render_template('return.html')


@app.route('/danger',methods=['POST'])
def danger():
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)