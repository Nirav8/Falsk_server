from flask import Blueprint
from flask.globals import request, session
from flask.json import jsonify

useraccount = Blueprint('useraccount' , __name__)

@useraccount.route("/logout", methods = ['GET', 'POST'])
def logout():
    print(session)
    session.pop('_username', None)
    print(session)
    return jsonify(),301