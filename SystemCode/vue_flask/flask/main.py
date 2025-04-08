from flask import Flask
from flask_login import LoginManager
from models import db
from config import Config
from register import UserRegister
from login import UserLogin
from facial import UserVideo
from flask_restful import Resource, Api
from flask_cors import CORS
from nap import UserNap
from lean import UserLean
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
api = Api(app)
CORS(app)

api.add_resource(UserNap,'/nap')
api.add_resource(UserLogin,'/user')
api.add_resource(UserRegister,'/register')
api.add_resource(UserLean,'/lean')
api.add_resource(UserVideo,'/video')

if __name__ == '__main__':
    app.run(debug=True)

