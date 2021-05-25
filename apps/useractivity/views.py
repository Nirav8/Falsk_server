from flask import Blueprint, request
from flask.json import jsonify
from flask import session

activity = Blueprint('useractivity' , __name__)

@activity.route('/home', methods=['GET'])
def Home():
    print(request.headers['Cookie'])
    return jsonify('welcome to social connect')

