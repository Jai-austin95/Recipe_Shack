from flask_pymongo import PyMongo
import json

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "name here"
app.config["MONGO_URI"] = "MONGO_URL"

mongo = PyMongo(app)