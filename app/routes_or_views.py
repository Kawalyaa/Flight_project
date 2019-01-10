# The next line means from app the folder import app the object of flask
from flask import jsonify, request, abort, make_response
from app import app
my_flights = [
    {
        'flightId': 1,
        'destination': u'new york',
        'duration': 500
    },
    {
        'flightId': 2,
        'destination': u'Toronto',
        'duration': 300
    }
]

from tests import errors


@app.route('/all_flights', methods=['GET'])
def all_flights():
    # This fuvtion shows all my_flights
    return make_response(jsonify(
        {
            'status': "ok",
            'message': "Success",
            'my_flights': my_flights
        }), 200
    )


@app.route('/get_oneFlight/<int:id>', methods=['GET'])
def get_oneFlight(id):
    for aflight in my_flights:
        if aflight['flightId'] == id:
            return jsonify({'aflight': aflight})
    return jsonify({'message': 'not found'})
