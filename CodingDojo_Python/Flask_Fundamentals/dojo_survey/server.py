from flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def dojoSurvey():
    return render_template('index.html')

@app.route('/result', methods = ['post'])
def surveyResult():
    if len(request.form['name']) < 1:
        flash("Enter your name please")
        return redirect('/')

    if len(request.form['comment']) < 1:
        flash("Cannot leave comment box empty")
        return redirect('/')

    elif len(request.form['comment']) > 120:
        flash("Do not wirte more than 120 letters")
        return redirect('/')

    print "*********Got Post Info"
    n = request.form['name']
    loc = request.form['location']
    lang = request.form['language']
    comm = request.form['comment']

    return render_template('/result.html', name = n, location = loc, language = lang, comment = comm)

@app.route('/')
def backToSurvey():
    return redirect('index')

app.run(debug=True)
