from flask import Flask, send_file, Response,jsonify
from sqlalchemy import desc
from models import db, Facial
from config import Config
import numpy as np
import cv2
from flask_restful import Resource, Api
from flask_cors import CORS
import mysql
import base64

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
api = Api(app)
CORS(app)

def convert_blob_to_base64(blob_data):
    # Convert BLOB data to Base64-encoded strings
    base64_image = base64.b64encode(blob_data).decode()
    return base64_image

class UserVideo(Resource):

    def get(self):
        
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT image_data FROM images ORDER BY id DESC LIMIT 1')
        latest_image_data = cursor.fetchone()[0]

        return Response(latest_image_data, mimetype='image/jpeg')
    
# api.add_resource(UserVideo,'/video')

# if __name__ == '__main__':
#     app.run(debug=True)

