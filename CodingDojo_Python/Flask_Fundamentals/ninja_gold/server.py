from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
import random
from datetime import datetime



@app.route('/')
def index():
    if 'totalgold' not in session:
        session['totalgold'] = 0
    if 'adventures' not in session:
        session['adventures'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
    # print "******Processing*****", request.form['building']
    if request.form['building'] == "farm":
        newgold = random.randrange(10, 21)
    elif request.form['building'] == "cave":
        newgold = random.randrange(5, 11)
    elif request.form['building'] == "house":
        newgold = random.randrange(2, 6)
    else:
        newgold = random.randrange(-50, 51)
    # print"*****got gold*****", newgold
    session['totalgold'] += newgold
    time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    if newgold >= 0:
        adventure = "Earned {} from the {}! {}".format(newgold, request.form['building'], time)
    else:
        adventure = "Entered a {} and lost {} gold...{}".format(newgold, request.form['building'], -1 * newgold, time)
    session['adventures'].append(adventure)
    print"Adventures array", session['adventures']
    return  redirect('/')

app.run(debug = True)
