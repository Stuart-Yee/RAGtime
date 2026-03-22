from flask import Flask, render_template, session, flash, redirect, request
from RAGtime import app
# from flask_bcrypt import Bcrypt
# from flask_app.models.user import User
# bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")
