from flask import Flask, request, redirect, render_template, session, jsonify
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
from flask_cors import CORS
from config import Config
from models import db
import pymysql
import base64
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Setting the application key for encrypting session data
app.config.from_object(Config)
db.init_app(app)
api = Api(app)
CORS(app)

def encode_string(string):
    encoded_string = base64.b64encode(string.encode()).decode()
    return encoded_string

# decrypt a string
def decode_string(encoded_string):
    decoded_string = base64.b64decode(encoded_string).decode("ISO-8859-1")
    return decoded_string

# Configuring MySQL Database Connections
db = pymysql.connect(
    host='localhost',
    user='root',
    password='123',
    database='users'
)

# Define login page routing
class UserLogin(Resource):
    # Get current user's username, password, phone number and user's photo
    def get(self):
            db = pymysql.connect(
                host='localhost',
                user='root',
                password='123',
                database='users'
            )
            cursor = db.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id, username, password FROM user2")
            user = cursor.fetchall()

            decoded_data = []
            for user in user:
                decoded_user = {
                'id': user['id'],
                'username': user['username'],
                'password': decode_string(str(user['password']))
                }
                print(decoded_user)
                decoded_data.append(decoded_user)

            return jsonify(decoded_data)
    
         


