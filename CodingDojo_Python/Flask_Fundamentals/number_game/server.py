from flask import Flask, render_template, request, redirect, session, url_for
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():
    if "win_number" not in session:
        session["win_number"] = random.randrange(1,101)
    elif session["win_number"] == session["guess"]:
        session.pop("win_number")
        session.pop("guess")
        session.pop("test")
        return redirect("/")
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    session["guess"] = int(request.form["guess"])
    if session["guess"] == session["win_number"]:
        session["test"] = str(session["win_number"]) + " was the number!"
        return redirect("/repeat")
    if session["guess"] > session["win_number"]:
        session["test"] = "Too High!"
    if session["guess"] < session["win_number"]:
        session["test"] = "Too Low!"
    return redirect("/")

@app.route("/repeat")
def repeat():
    return render_template("index.html")
app.run(debug=True)
