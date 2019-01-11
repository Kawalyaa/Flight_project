# The next line means from app the folder import app the object of flask
from flask import jsonify, request, abort, make_response
from app import app
my_flights = [
    {
        'flightId': 1,
        'destination': 'new york',
        'duration': 500
    },
    {
        'flightId': 2,
        'destination': 'Toronto',
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

# This route creates aflight and adds it to my_flight list


@app.route('/create_aflight', methods=['POST'])
def create_aflight():
    if not request.json or 'destination' not in request.json:
        abort(400)
    flight = {
        'flightId': my_flights[-1]['flightId'] + 1,
        'destination': request.json['destination'],
        'duration': request.json['duration']

    }
    my_flights.append(flight)
    return jsonify(
        {
            'flight': flight,
            'message': 'created'
        }), 201

# This route updets the flight if it exists in the list


@app.route('/update_flight/<int:ask_flightId>', methods=['PUT'])
def update_flight(ask_flightId):
    if not request.json:
        abort(400)
    for aflight in my_flights:
        if aflight['flightId'] == ask_flightId:
            aflight['destination'] = request.json.get('destination', aflight['destination'])

            aflight['duration'] = request.json.get('duration', aflight['duration'])
            return jsonify(
                {
                    'aflight': aflight,
                    'message': 'Flight updated'
                })

    return jsonify({'message': 'Id not found'}), 404

    # This route handles the delete function


@app.route('/remove_aflight/<int:flightId>', methods=['DELETE'])
def remove_aflight(flightId):
    for aflight in my_flights:
        if aflight['flightId'] == flightId:
            my_flights.remove(aflight)
            return jsonify(
                {
                    'result': True,
                    'message': 'Deleted'
                })

    return jsonify({'message': 'id not found'}), 404
