from apps import check_email, compare_hash
from flask import Blueprint, request, render_template, redirect
from flask.json import jsonify
from .model import _isuser
from flask import session

login = Blueprint('login', __name__)

@login.route('/user', methods =['GET' , 'POST'])
def Login():
    try:
        if request.method == 'GET':
            return render_template('login/login.html')

        elif request.method == 'POST':
            _json = request.json
            _username = _json['username']
            _isemail = check_email(_username)

            _user = _isuser(isemail = _isemail, username = _username)

            if _user == None:
                return jsonify("user not exist"), 450

            else:
                __password = _json['password']
                _ans = compare_hash(_user['password'], __password)

                if _ans == True:
                    session['_username'] = _username
                    return jsonify({"message" : "login sucsess fully"}), 201

                else:
                    return jsonify({'result': 'password is not correct'}), 451
    except Exception as ex:
        print(ex, "**************************")

