#!/usr/bin/env python
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dateutil import parser
from datetime import timedelta
from config import app, rpc, db, SECRET, PORT
from models import Event

def timetable_add(username, event):
    parsed_time = parser.parse(event['time'])
    newEvent = Event(username, event['name'], parsed_time)
    db.session.add(newEvent)
    db.session.commit()
    return {'successful' : newEvent != None}

def timetable_get(username, date):
    new_date = parser.parse(date)
    end_date = new_date + timedelta(days=7)
    user = Event.query.filter_by(username = username)
    time = user.filter(Event.time.between(str(new_date), str(end_date)))
    results = []
    for x in time.all():
        result = {}
        result["username"] = x.username
        result["description"] = x.description
        result["time"] = x.time.isoformat()
        results.append(result)
    return results

@app.route('/', methods=["POST"])
def handle():
    return jsonify(rpc(request.json))

@app.route('/create', methods=["POST"])
def create():
    if request.json["secret"] == SECRET:
        db.create_all()
    return jsonify("Successful")

if __name__ == "__main__":
    rpc['Timetable.add'] = timetable_add
    rpc['Timetable.get'] = timetable_get
    app.run(host='0.0.0.0', port=PORT)
