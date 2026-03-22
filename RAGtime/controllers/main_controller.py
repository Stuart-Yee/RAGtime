from flask import render_template, session, flash, redirect, request
from RAGtime import app


@app.route("/")
def index():
    print("route started")
    return render_template("index.html")