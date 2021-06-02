from flask import Flask
from flask.globals import session
from flask.helpers import url_for
from flask_cors import CORS
from flask_session import Session
from flask_redis import FlaskRedis
import redis

from apps.signin.views import login
from apps.signup.views import signup
from apps.useractivity.views import activity
from apps.useraccount.views import useraccount

app = Flask(__name__)

redis = FlaskRedis(app)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
# app.config['SESSION_USE_SIGNER'] = True
app.config['SECRET_KET'] = "#22253%6DFvskleg$2%^7birsmgw77%55##"
# app.config['SESSION_REDIS'] = redis.from_url('redis://localhost:6379')

app.register_blueprint(login , url_prefix = '/login')
app.register_blueprint(signup , url_prefix = '/signup')
app.register_blueprint(activity, url_prefix='/user')
app.register_blueprint(useraccount, url_prefix='/account')

#from cross platform
CORS(app)
Session(app)

session = Session()

if __name__ =='__main__':
    session.init_app(app)
    app.run(debug=True,threaded= True)
