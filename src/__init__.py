from flask import Flask, jsonify, json
from flask_cors import CORS
from flask_pymongo import PyMongo
import json
from bson import json_util

app = Flask(__name__)
CORS(app)

## Setting database
import pymongo

# Production Environment
database = pymongo.MongoClient("mongodb+srv://eugenio:mateus1234@cluster0-8jxzv.mongodb.net/test?retryWrites=true&w=majority/")

# Development Environment
#database = pymongo.MongoClient("mongodb://localhost:27017/")

users = database["users"]["customers"]

#Get all users from DB
@app.route('/v1/users')
def get():
    response = []
    for i in users.find():
        response.append(i)
        
    return json.dumps(response, default=json_util.default)