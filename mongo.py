import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient()

db = client.phones

samsung = db.samsung

db.samsung.insert_one({
    "title": "A50",
    "ram": "64",
    "camera": [
        64,
        32,
        16,
    ],
    "price": 500,
    "url": "https://realpython.com/python-csv/"
})

for doc in samsung.find():
    pprint.pprint(doc)