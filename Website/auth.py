from flask import Blueprint
from flask.templating import render_template

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("Website\Templates\login.html")

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up")
def sign_up():
    return render_template("Website\Templates\sign_up.html")