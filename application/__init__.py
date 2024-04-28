from flask import Flask
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient

app = Flask(__name__)
app.config["SECRET_KEY"] = "996bf76dae69e6da2cf1287d083f74a352c77b21"
# app.config["MONGO_URI"] = "mongodb+srv://abhinandmukundan15:<abhinandmukundan15>@cluster0.nttfi0k.mongodb.net/"
app.config["MONGO_URI"] = "mongodb+srv://abhinandmukundan15:abhinandmukundan15@cluster0.nttfi0k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# app.config["MONGO_URI"] = "mongodb+srv://akarshkonniyoor:<qoUj2D8ciQ1rbOGt>@cluster0.jah2qxe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# app.config["MONGO_URI"]="mongodb://localhost:27017/todo"
# mongodb database
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes

uri = "mongodb+srv://akarshkonniyoor:qoUj2D8ciQ1rbOGt@cluster0.jah2qxe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
