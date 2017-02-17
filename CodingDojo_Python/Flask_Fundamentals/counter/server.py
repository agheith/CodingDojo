from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():

    if "counter" not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1

    return render_template('index.html', counter=session['counter'])

@app.route('/show', methods=['POST'])
def show():
    if request.form['button'] == 'Add 2':
        session['counter'] += 1

    if request.form['button'] == 'reset':
        session['counter'] = 0

    return redirect('/')

app.run(debug=True)
