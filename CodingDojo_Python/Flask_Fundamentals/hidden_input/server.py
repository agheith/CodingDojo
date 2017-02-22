from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

# @app.route('/')
#
# if request.form['action'] == 'register':
#   //do registration process
# elif request.form['action'] == 'login':
#   //do login process
#   return render_template('index.html')

@app.route('/process', methods=['POST'])
def hiddenInput():
    if request.form['action'] == 'register':
        # do registration process
        
    elif request.form['action'] == 'login':
        # do login process

app.run(debug=True)
