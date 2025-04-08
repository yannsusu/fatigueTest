from models import db
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from config import Config
import pymysql
import base64

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Setting the application key for encrypting session data
app.config.from_object(Config)
db.init_app(app)
api = Api(app)
CORS(app)

db = pymysql.connect(
    host='localhost',
    user='root',
    password='123',
    database='users'
)

# encrypted string
def encode_string(string):
    encoded_string = base64.b64encode(string.encode()).decode()
    return encoded_string

# decrypt a string
def decode_string(encoded_string):
    decoded_string = base64.b64decode(encoded_string).decode()
    return decoded_string

class UserRegister(Resource):

    def post(self):
        db = pymysql.connect(
                host='localhost',
                user='root',
                password='123',
                database='users'
            )
        username = request.json.get('username')
        password = request.json.get('password')
        password = encode_string(str(password))

        # Encrypting information
        encoded_password = encode_string(password)

        # Check if the username already exists
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM user2 WHERE username=%s', (username))
        user = cursor.fetchone()
        if user:
        # User already exists
            return jsonify({'message': '用户名已经存在'})

        cursor.execute('INSERT INTO user2 (username, password) VALUES (%s, %s)', (username, password))
        db.commit()

        return jsonify({'message': '注册成功'})
