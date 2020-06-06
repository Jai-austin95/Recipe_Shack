import os
from flask import Flask, redirect, url_for, render_template, request
from flask_pymongo import PyMongo
from os import path
if path.exists("env.py"):
  import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'DB_NAME'

app.config["MONGO_URI"] = 'SECRETKEY'

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def homepage():
    return render_template("home.html")

@app.route("/catergories")
def catergories():
    return render_template("catergories.html")

@app.route("/recipe/id")
def recipe():
    return render_template("recipe.html")

@app.route("/add-recipe")
def addrecipe():
    return render_template("add-recipe.html")


if __name__ == "__main__":
    app.run(debug=True)
