from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
import json
from bson import json_util

app = Flask(__name__)
CORS(app)

## Setting database
import pymongo

# Production Environment
database = pymongo.MongoClient("mongodb+srv://eugenio:mateus1234@cluster0-8jxzv.mongodb.net/test?retryWrites=true&w=majority")

# Development Environment
#database = pymongo.MongoClient("mongodb://localhost:27017/")

users = database["users"]["customers"]

#Get all users from DB
@app.route('/api/users', methods=['GET'])
def get_users():
    response = []
    for i in users.find():
        response.append(i)
        
    return json.dumps(response, default=json_util.default)

#Create new user
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()

    obj = {
        "name": data["name"],
        "last_name": data["last_name"],
        "age": data["age"],
        "role": data["role"],    
        "games": data["games"],
        "contacts": data["contacts"]
    }

    print(obj)

    res = users.insert_one(obj)

    return jsonify({
        "message": 'User added on ${}'.format(res)
    })

#Delete user
@app.route('/api/delete/<name>', methods=['DELETE'])
def remove(name):
    print(name)

    users.delete_one({"name": name})

    return jsonify({
        "message": "{} removed".format(name)
    })

#Update user
@app.route('/api/update/<name>', methods=["PUT"])
def update(name):

    data = request.get_json()
    
    query = {"name": name}
    
    users.update_one(query, {"$set": data}) 

    return jsonify({
        "message": "{} edited!".format(name)
    })

#GET unique user
@app.route('/api/user/<name>', methods=["GET"])
def get_user(name):
    
    response = users.find_one({"name":name})

    return json.dumps(response, default=json_util.default)