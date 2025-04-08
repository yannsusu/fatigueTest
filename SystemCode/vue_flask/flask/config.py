# config.py
class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@localhost/users'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
    UPLOAD_FOLDER = 'photos'
    FACIAL_FOLDER = 'video'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
