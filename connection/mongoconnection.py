import pymongo
from pymongo import mongo_client

try:
    mongo = pymongo.MongoClient(
        host='localhost',
        port = 27017
    )
    print(mongo.server_info)
except Exception as ex:
    print("database connection error")