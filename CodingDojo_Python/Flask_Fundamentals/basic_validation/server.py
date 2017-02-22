from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    #do the validation here...
    if len(request.form['name']) < 1:
        flash("Name cannot be empty")
        # print"*****invalid name*****"
    else:
        flash("Success, your name is {}".format(request.form['name']))
        # print"*****name is valid*****"
    return redirect('/')

app.run(debug=True)
