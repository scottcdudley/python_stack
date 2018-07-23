from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    print('Strawberry', request.form['strawberry'])
    print('Raspberry', request.form['raspberry'])
    print('Apple', request.form['apple'])
    print('First Name', request.form['first_name'])
    print('Last Name', request.form['last_name'])
    print('Student ID', request.form['student_id'])
    total = int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple'])
    print(total)
    return render_template("checkout.html", total = total)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")



if __name__=="__main__":   
  app.run(debug=True) 