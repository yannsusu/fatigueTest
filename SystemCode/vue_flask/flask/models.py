from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, LargeBinary, String, DateTime


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    user_photo = db.Column(db.String(255))

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Nap(db.Model):
    __tablename__ = 'nap'

    time = db.Column(db.DateTime, primary_key=True, default=datetime.utcnow)
    blink = db.Column(db.Float, nullable=False)
    yawn = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Nap time={self.time}, blink={self.blink}, yawn={self.yawn}>'
    
class Lean(db.Model):
    __tablename__ = 'Microbit'

    time = db.Column(db.DateTime, primary_key=True, default=datetime.utcnow)
    angle = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Nap time={self.time}, blink={self.blink}, yawn={self.yawn}>'


class Facial(db.Model):
    __tablename__ = 'facial'

    time = Column(DateTime, primary_key=True, default=datetime.utcnow)
    video = Column(LargeBinary)
    name = Column(String)

    def __repr__(self):
        return f"Facial(time={self.time}, name='{self.name}')"









