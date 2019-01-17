from flask import make_response, jsonify
from app import app


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': "Bad request"}, 400))


@app.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({'message': 'Intternal internal_server_error or check spelling'}, 500))
