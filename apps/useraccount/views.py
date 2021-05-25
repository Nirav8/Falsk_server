from typing_extensions import Required
from flask import Blueprint
from flask.globals import request, session
from flask.json import jsonify
from .model import *

useraccount = Blueprint('useraccount' , __name__)

@useraccount.route("/logout", methods = ['GET', 'POST'])
def logout():
    print(session)
    session.pop('_username', None)
    print(session)
    return jsonify(),301

#TODO create an decorator and make is secure
#TODO maek template for changing password
@useraccount.route("/changepassword", methods=['GET', 'POST'])
def changepassword():
    if request.method == 'GET':
        return jsonify('comming soon'), 501
    elif request.method == 'POST':
        _json = request.json
        _email = _json['email']
        
        _user = _isuser(_email)
        
        if _user:
            compare_hash(_user['password'])
            

