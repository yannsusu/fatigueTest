from flask import Flask, jsonify, request
from sqlalchemy import desc
from time import sleep
from flask_restful import Resource, Api
from models import db, Lean
from flask_cors import CORS
from config import Config
from sqlalchemy import text


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
api = Api(app)
CORS(app)
latest_data = None

def GetNumber(string):
    numeric_part = string.split('=')[1].split('.')[0]
    number = float(numeric_part)
    return number


# Routing: Getting real-time data
class UserLean(Resource):

    def get(self):
    # Query the latest ten sets of data and sort them by time
        
        latest_data_query = text("SELECT vepov FROM Microbit ORDER BY time DESC LIMIT 10")
        latest_data = db.engine.execute(latest_data_query).fetchall()

        data_array = []
        for row in latest_data:
            # Converting Data to Array Form
            angle = row[0]
            data_array.append([abs(GetNumber(str(angle)))])

        # If the query result is less than ten groups, use [0, 0] to make up for it
        while len(data_array) < 10:
            data_array.append([0])

        return jsonify(data_array)
    
# api.add_resource(UserLean,'/lean')

# if __name__ == '__main__':
#     app.run(debug=True)