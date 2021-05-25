from flask import json
from flask.templating import render_template
from pymongo.message import _insert
from apps import check_email, convert_hash
from flask import Blueprint, redirect
from flask.globals import request
from flask.json import jsonify
from .model import _istempuser, _insert, _isuser, _verifyuser

signup = Blueprint('signup' , __name__ )

@signup.route('/user', methods = ['GET' , 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template('signup/signup.html')
    elif request.method == 'POST':
        try:    
            _json = request.json
            _email = _json['email']
            _isemail = check_email(_email)

            if _isemail == False:
                return jsonify('not valid email')

            else:
                _tempuser = _istempuser(email = _email)
                _user = _isuser(email = _email)

                if _user == None and _tempuser !=None:
                    return jsonify({'result' : "email allredy in used, please verify your email"})
                
                elif _user != None and _tempuser == None:
                    return jsonify({
                        "message" : "Verify your email !!!!"
                    }), 201

                elif _tempuser == None and _user != None:
                    return jsonify({
                        "message" : "you are allredy verifid"
                    }), 200

                elif _user == None and _tempuser == None:
                    _username = _json['username']
                    _password = _json['password']
                    _password = convert_hash(_password)
                    _userdata = {
                            'username': _username,
                            "email": _email,
                            "password": _password,
                            }
                    inserted = _insert(_userdata)
                    #send email for verifying account

                    # emailsending(_email, _name, "http://localhost:9090/verify/{}?token={}".format(_email, _token))    
                    return jsonify({
                        'reult: ': "User Created",
                        'id' : inserted
                    })
        except Exception as ex:
            print("***************************************************")
            print(ex)
            print("***************************************************")

@signup.route("/verify/<userid>", methods = ['GET' , 'POST'])
#TODO:make decorator at hear
def verify(userid):
    if request.method == 'GET':
        return jsonify("we have nothing yet,,,"),204
    elif request.method == 'POST':
        verified = _verifyuser(userid=userid)
        print(verified)
        return jsonify('verified')
       

