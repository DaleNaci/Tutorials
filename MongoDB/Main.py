import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://admin:clubpenguin888@cluster0-af4ps.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

post = {
    "_id": 0,
    "name": "dale",
    "score": 5
}

collection.insert_one(post)
