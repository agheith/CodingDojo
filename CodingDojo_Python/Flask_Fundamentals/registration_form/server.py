from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NO_NUMBERS = re.compile(r"^[a-zA-Z'-]+$")

app = Flask(__name__)
app.secret_key = "ThisIsSecret"
@app.route('/', methods=['GET'])

def index():
    return render_template("index.html")

@app.route('/result', methods = ['POST'])
def submit():
    blankFields =['firstName','lastName','password','confirm']
    for field in blankFields:
        if len(request.form[field])< 1:
            flash("Cannot be empty")
            break

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")

    if not NO_NUMBERS.match(request.form["firstName"]):
        flash("Cannot have numbers or special symbols!")

    if not NO_NUMBERS.match(request.form["lastName"]):
        flash("Cannot have numbers or special symbols!")

    if len(request.form['password']) < 8:
        flash("Password should be more than 8 characters")

    if request.form['password'] != request.form['confirm']:
        flash("Passwords don't match")

    return redirect('/')


app.run(debug = True)
