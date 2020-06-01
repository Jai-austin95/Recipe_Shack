from flask import Flask, redirect, url_for, render_template

from flask_pymongo import PyMongo

import json

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "name here"
app.config["MONGO_URI"] = "MONGO_URL"

mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("home.html")
