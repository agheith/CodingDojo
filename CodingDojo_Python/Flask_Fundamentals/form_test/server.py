from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below

@app.route('/')

def index():
    return render_template("index.html")
#this route will handle our form submission

@app.route('/users/', methods = ['POST'])
#notice how we defined which http methods are allowed by this route
def create_user():
    print "***********Got post info"
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    #redirects back to the '/' route
    return redirect('/show')
# noticed that we changed where we redirect to so that we can go to the page that displays the name and email!

@app.route('/show/{{ name }}')
def show_user():
    return render_template('/user.html')
app.run(debug=True)
