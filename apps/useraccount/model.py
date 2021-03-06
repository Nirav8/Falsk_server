from apps import compare_hash, convert_hash
from connection.mongoconnection import mongo

users = mongo.Login.users

"""
we can implement hear for making it more convineant
like make possible with username too
"""
def _isuser(email):
    user = users.find_one({'email' : email})
    return user

def _changepassword(new_pass , email):
    try:
        users.update_one({"email" : email} , {'$set' : {"password" : new_pass}})
        return 1
    except Exception as ex:
        return ex

def _changeusername(email , newusername):
    try:
        users.update_one({'email' : email} , {'$set' : {'username' : newusername}})
        return 1
    except Exception as ex:
        return ex

def _isusernameavailabe(username):
    try:
        if users.find_one({"username" : username}):
            return False
        else:
            return True
    except Exception as ex:
        return True

