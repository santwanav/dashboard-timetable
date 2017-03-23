from uuid import uuid4
from config import db


class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(db.String(32), primary_key=True)
    username = db.Column(db.String(20))
    description = db.Column(db.String(250))
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)

    def __init__(self, username, description, start, end):
        self.id = uuid4().hex
        self.username = username
        self.description = description
        self.start = start
        self.end = end
