import os
from flask import Flask, redirect, url_for, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'recipe-shack'

app.config['MONGO_URI'] = 'mongodb+srv://root:EEB4A90F66@jaicluster-9bnub.mongodb.net/recipe-shack?retryWrites=true&w=majority'

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
