"""Flask middleware definitions. This is also where filters are defined."""

from flask import current_app, make_response, jsonify


@current_app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Data not found'}), 404)
