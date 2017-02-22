from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.secret_key='ThisisSecret'

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    users = 'Ninjas/tmnt.png'
    return render_template('index2.html', users=users)

@app.route('/ninja/<users>')
def im_ninja(users):
    if users == "blue":
        users = 'Ninjas/leonardo.jpg'
    elif users == "orange":
        users = 'Ninjas/michelangelo.jpg'
    elif users == "red":
        users = 'Ninjas/raphael.jpg'
    elif users == "purple":
        users = 'Ninjas/donatello.jpg'
    else:
        users = 'Ninjas/notapril.jpg'
    return render_template('ninja.html', users=users)
app.run(debug=True)
