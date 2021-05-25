from apps import compare_hash, convert_hash
from connection.mongoconnection import mongo

users = mongo.Login.users

"""
we can impen=ment hear for making it more convineant
like make possible with username too
"""
def _isuser(email):
    user = users.find_one({'email' : email})
    return user


def _changepassword(new_pass , email):
    try:
        users.update_one({"email" : email} , {'$set' : {{"password" : convert_hash(new_pass)}} })
        return 1
    except Exception as ex:
        return ex