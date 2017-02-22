from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'emaildb')
app.secret_key = "ThisIsSecret"

@app.route("/")
def  index():
    # allemails = mysql.query_db("SELECT * FROM emails")
    # print "got all the emails", allemails
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def process():
    EMAIL_REGEX=re.compile(r'^[a-zA-Z-0-9.+_-]+@[a-zA-Z-0-9._-]+\.[a-zA-z]+$')
    useremail = request.form['email']
    if EMAIL_REGEX.match(useremail):#if the input email matches the REGEX
        # print "Valid Email", email --> print to see if the email is valid
        myquery = "INSERT INTO emails (email, created_at, updated_at) VALUES (:user_input, NOW(), NOW())"
        mydata = {"user_input": useremail}
        newuserid = mysql.query_db(myquery, mydata) #insert into the db
        flash("The email you entered ({}), is a valid email address!! Thank you!".format(useremail))
        print "we have a valid email", newuserid
        return redirect('/success')
    else:
        print "Not Valid", useremail
        flash("Not a valid email")
# #printed this in the terminal to verify our work
    return redirect('/')


@app.route("/success")
def success():
    allemails = mysql.query_db("SELECT * FROM emails")
    print "all the emails", allemails
    for em in allemails:
        em['created_at'] = em['created_at'].strftime("%m/%d/%Y %I:%M %p")
    return render_template("success.html", emails = allemails) #pass them to the HTML page with emails = allemails

app.run(debug=True)
