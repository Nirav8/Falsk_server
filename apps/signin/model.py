from connection.mongoconnection import mongo

users = mongo.Login['users']
temp_user = mongo.Login['temp_users']

def _isuser(isemail, username):

    if isemail == True:
        _user = users.find_one({'email' : username})
        _temp = temp_user.find_one({'email' : username})
        if _temp:
            return '201'

    elif isemail == False:
        _user = users.find_one({'username' : username})
        _temp = temp_user.find_one({'username' : username})
        if _temp:
            return '201'
    
    a = users.find_one({'email' : 'namorgit removeadiya99@gmail.com'})
    return _user

    