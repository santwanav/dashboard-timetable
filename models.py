from config import db
from datetime import datetime

class Event(db.Model):
    __tablename__ = 'event'

    username = db.Column(db.String(20), primary_key = True)
    description = db.Column(db.String(250), primary_key = True)
    time = db.Column(db.DateTime, primary_key = True)

    def __init__(self, username, description, time):
        self.username = username
        self.description = description
        self.time = time
