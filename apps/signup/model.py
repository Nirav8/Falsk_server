from bson.objectid import ObjectId
from connection.mongoconnection import mongo

temp_user = mongo.Login.temp_users
users = mongo.Login.users

def _isuser(email):
    user = users.find_one({'email' : email})
    return user

def _istempuser(email):
    tempuser = temp_user.find_one({'email' : email})
    return tempuser

def _insert(data):
    inserted = temp_user.insert_one(data)
    _new_id = inserted.inserted_id
    return _new_id

def _verifyuser(userid):
    user = temp_user.find_one({'_id' : ObjectId(userid)})
    user.pop('_id')
    try:
        temp_user.delete_one({'_id' : ObjectId(userid)})
    except Exception as ex:
        return ex
    added = users.insert_one(user)
    return added