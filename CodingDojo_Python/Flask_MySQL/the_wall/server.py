from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
EMAIL_REGEX=re.compile(r'^[a-zA-Z-0-9.+_-]+@[a-zA-Z-0-9._-]+\.[a-zA-z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'dojo_wall')
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if 'id' in session:
        print"*********current id in session*********", session['id']
    else:
        print"**************no session*********"
    all_users = mysql.query_db("SELECT * FROM users")
    return render_template("index.html", all_users = all_users)

@app.route('/login', methods=['post'])
def login():
    all_users = mysql.query_db("SELECT * FROM users")
    for i in all_users:
        if i['email'] == request.form['email']:
            print "**************email match**************"
            if bcrypt.check_password_hash(i['password'], request.form['password']):
                print "************password match**************"
                session['id'] = i['id']
                return redirect('/success')
    flash("Your user info does not match our database. Please try again.")
    return redirect('/')

@app.route('/success')
def success():
    # check if the user is in session
    if "id" in session:
        query = "SELECT * FROM users WHERE id={}".format(session['id'])
        username = mysql.query_db(query)[0]['first_name']
        # get the username by using the id in session
        fetchquery = "SELECT first_name, last_name, messages.id, messages.message, messages.created_at FROM users JOIN messages ON users.id = messages.user_id ORDER BY created_at DESC;"
        # fetch query to get all the messages
        allmessages = mysql.query_db(fetchquery)
        for messages in allmessages:
            message['created_at'] = message['created_at'].strftime('%B %d %Y')

        commentquery = "SELECT users.first_name, users.last_name, comments.comment, comments.created_at, comments.message_id FROM comments JOIN users ON users.id = comments.user_id ORDER BY created_at ASC;"
        # get all the comments
        allcoments = mysql.query_db(commentquery)
        for comment in allcoments:
            comment['created_at'] = comment['created_at'].strftime('%B %d %Y')
        print "*****got all comment*****", allcoments
        return render_template("success.html", username = username, msgs = allmessages, comments = allcoments)
    else:
        flash("Please log in to continue")
        return redirect('/')

@app.route('/log_out')
def log_out():
    session.pop('id')
    flash("You have now logged out, Have a great day!")
    return redirect('/')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/process', methods = ['post'])
def create_user():
    print "************created user**********"
    error = 0

    def hasNumbers(inputString):
        return any(char.isdigit() for char in inputString)
        #This function is a helper function

    if len(request.form["email"]) == 0:
        flash("Please insert a valid email address. Try again.")
        error = 1
    else:
        all_users = mysql.query_db("SELECT * FROM users")
        for i in all_users:
            if i ['email'] == request.form['email']:
                flash("This email address is already taken, please choose a different email")
                error = 1

    if len(request.form["first_name"]) < 2:
        flash("Please enter your first name")
        error = 1
    elif hasNumbers(request.form["first_name"]) == True:
        flash("Do not enter numeric values")
        error = 1

    if len(request.form["last_name"]) < 2:
        flash("Please enter your lsat name")
        error = 1
    elif hasNumbers(request.form["last_name"]) == True:
        flash("Do not enter numeric values")
        error = 1

    if len(request.form['password']) == 0:
        flash("Password must be more than 8 characters")
        error = 1
    elif (request.form['password']) != (request.form['confirm']):
        flash("please verify that both passwords match.")
        error = 1

    if error == 0:
        insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
            "first_name":request.form['first_name'],
            "last_name":request.form['last_name'],
            "email":request.form['email'],
            "password":bcrypt.generate_password_hash(request.form["password"])
        }

        newid = mysql.query_db(insert_query, data)
        session['id'] = newid
        return redirect('/success')

    print "************processed*********"
    return redirect("/registration")

@app.route('/create_message', methods=['post'])
def createMessage():
    userinput=request.form['message']
    if len(userinput)>0:
        insert_query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :id)" #she used those colons as placeholders to replace them with user's input
        data = {
            'message': userinput,
            # the key of message should be whatever the user's input is
            'id':session['id']
        }
        mynewmessageid = mysql.query_db(insert_query, data)
        print "********got the new message******", mynewmessageid
        #insert it to the database
    else:
        print"nothing in the input field"
    return redirect('/success')

@app.route('/create_comment', methods=['post'])
def createComment():
    print "**********created comment********", request.form
    insert_query = "INSERT INTO comments (comment, user_id, message_id, created_at, updated_at) VALUES (:comment, :userid, :messageid, NOW(), NOW());"
    data = {
        "comment":request.form['comment'],
        "userid":request.form['id'],
        "messageid":request.form['msgid']
    }
    # gotta pass into mysql
    mysql.query_db(insert_query, data)
    return redirect('/success')



app.run(debug=True)
