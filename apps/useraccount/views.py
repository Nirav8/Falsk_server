from pymongo.collection import ReturnDocument
from apps import compare_hash, convert_hash, login_required
from flask import Blueprint
from flask.globals import request, session
from flask.json import jsonify

from .model import _isuser, _changepassword, _changeusername, _isusernameavailabe

useraccount = Blueprint('useraccount' , __name__)

@useraccount.route("/logout", methods = ['GET', 'POST'])
def logout():
    session.clear()
    return jsonify(),301
    

#TODO create an decorator and make is secure
#TODO maek template for changing password

@useraccount.route("/changepassword", methods=['GET', 'POST'])
@login_required
def changepassword():
    if request.method == 'GET':
        return jsonify('comming soon'), 501
    elif request.method == 'POST':
        _json = request.json
        _email = _json['email']
        _user = _isuser(_email)
        
        if _user:
            _iscorrect = compare_hash(_user['password'], _json['password'])
            if _iscorrect:
                _ischanged = _changepassword(convert_hash(_json['new_password']), _email)
                if _ischanged:
                    return jsonify({'message': 'changed'}), 200
                else:
                    return jsonify(), 304
            else:
                return jsonify({'message' : 'password ios incorret'}), 451

@useraccount.route("/changeusername", methods=['GET' , 'POST'])
@login_required
def changeusername():
    if request.method == 'GET':
        return jsonify(), 501

    elif request.method == 'POST':
        _json = request.json
        _username = _json['email']
        _newusername = _json['new_username']
        
        _isavailable = _isusernameavailabe(_newusername)

        if _isavailable:
            if _changeusername(_username, _newusername):
                return jsonify(), 204

        else:
            return jsonify(),  401
