#!/usr/bin/env python
from flask import request, jsonify
from dateutil import parser
from config import app, rpc, db, SECRET, PORT
from models import Event
from sqlalchemy import or_


def timetable_add(params):
    username = params['username']
    event = params['event']
    parsed_start = parser.parse(event['start'])
    parsed_end = parser.parse(event['end'])
    newEvent = Event(username, event['name'], parsed_start, parsed_end)
    db.session.add(newEvent)
    db.session.commit()
    return {'successful': newEvent is not None}


def timetable_get(params):
    username = params['username']
    start = params['start']
    end = params['end']
    new_date = parser.parse(start)
    end_date = parser.parse(end)
    user = Event.query.filter_by(username=username)
    time = user.filter(or_(Event.start.between(str(new_date), str(end_date))),
                       Event.end.between(str(new_date), str(end_date)))
    results = []
    for x in time.all():
        result = {}
        result["id"] = x.id
        result["description"] = x.description
        result["start"] = x.start.isoformat()
        result["end"] = x.end.isoformat()
        results.append(result)
    return results


@app.route('/', methods=["POST"])
def handle():
    result = rpc(request.json)
    return jsonify(result)


@app.route('/create', methods=["POST"])
def create():
    if request.json["secret"] == SECRET:
        db.create_all()
    return jsonify("Successful")


if __name__ == "__main__":
    rpc['Timetable.add'] = timetable_add
    rpc['Timetable.get'] = timetable_get
    app.run(host='0.0.0.0', port=PORT)
