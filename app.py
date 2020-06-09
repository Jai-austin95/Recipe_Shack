import os
from flask import Flask, render_template, url_for, redirect
from flask_pymongo import PyMongo

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("NONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def homepage():
    return render_template("home.html")

@app.route("/catergories")
def catergories():
    return render_template("catergories.html")

@app.route("/recipe/<id>")
def recipe(id=None):
    print(id)
    return render_template("recipe.html", recipe=mongo.db.recipes.find())

@app.route("/add-recipe")
def addrecipe():
    return render_template("add-recipe.html")

@app.route("/test")
def test():
    recipes = mongo.db.recipes.find()
    print(recipes)
    return render_template("test.html", recipes = recipes)



if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
