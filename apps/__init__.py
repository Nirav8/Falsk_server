import re
import hashlib
from flask import session
from functools import wraps

from flask.json import jsonify

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def check_email(email):
    m = re.search(regex, email)
    if m:
        return True
    else:
        return False

def convert_hash(a):
    a = str(a)
    a = bytes(a, 'utf-8')
    return(hashlib.sha256(a).hexdigest())

def compare_hash(old,new):
    new = convert_hash(new)
    if old == new:
        return True
    else:
        return False

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if '_username' in session:
            return f(*args, **kwargs)
        else:
            return jsonify({"message": "Login Requierd"}), 401
    return wrap

