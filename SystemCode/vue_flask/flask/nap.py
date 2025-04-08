from flask import Flask, jsonify, request
from sqlalchemy import desc
from time import sleep
from flask_restful import Resource, Api
from flask_cors import CORS
from models import db, Nap
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
api = Api(app)
CORS(app)
latest_data = None

# Routing: Getting real-time data
class UserNap(Resource):

    def get(self):
    # Query the latest ten sets of data and sort them by time
        latest_data = db.session.query(Nap.blink, Nap.yawn).order_by(desc(Nap.time)).limit(10).all()
        data_array = []
        
        for blink, yawn in latest_data:
            # Converting Data to Array Form
            data_array.append([blink, yawn])

        # If the query result is less than ten groups, use [0, 0] to make up for it
        while len(data_array) < 10:
            data_array.append([0, 0])

        return jsonify(data_array)
    