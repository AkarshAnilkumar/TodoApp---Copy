from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "996bf76dae69e6da2cf1287d083f74a352c77b21"
# app.config["MONGO_URI"] = "mongodb+srv://abhinandmukundan15:<abhinandmukundan15>@cluster0.nttfi0k.mongodb.net/"
app.config["MONGO_URI"] = "mongodb+srv://abhinandmukundan15:<password>@cluster0.nttfi0k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# app.config["MONGO_URI"]="mongodb://localhost:27017/todo"
# mongodb database
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes
