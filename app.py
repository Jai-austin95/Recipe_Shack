import os
from flask import Flask, render_template, url_for, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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

@app.route("/catergories/breakfast")
def breakfast():
    recipes = mongo.db.recipes.find({'typemeal': 'Breakfast'})
    return render_template("breakfast.html", recipes=recipes)

@app.route("/catergories/lunch")
def lunch():
    recipes = mongo.db.recipes.find({'typemeal': 'Lunch'})
    return render_template("lunch.html", recipes=recipes)

@app.route("/catergories/dinner")
def dinner():
    recipes = mongo.db.recipes.find({'typemeal': 'Dinner'})
    return render_template("dinner.html", recipes=recipes)

@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipes)

@app.route("/add-recipe")
def addrecipe():
    categories = mongo.db.Categories.find()
    return render_template("add-recipe.html", categories = categories)

@app.route("/insert_recipe", methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('homepage'))

@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    edit_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = list(mongo.db.Categories.find())
    return render_template("edit_recipe.html", edit=edit_recipe, categories = categories)

@app.route("/update_recipe/<recipe_id>", methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'name': request.form.get('name'),
        'smalldescription': request.form.get('smalldescription'),
        'typemeal': request.form.get('typemeal'),
        'image': request.form.get('image'),
        'preperationtime': request.form.get('preperationtime'),
        'cookingtime': request.form.get('cookingtime'),
        'ingredients': request.form.get('ingredients'),
        'preperations':request.form.get('preperations')
    })
    return redirect(url_for('homepage'))

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('homepage'))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)