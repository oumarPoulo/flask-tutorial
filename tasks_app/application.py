"""Holds the create_app() Flask application factory. More information in create_app() docstring."""

import logging
from importlib import import_module
from flask import Flask
from tasks_app.blueprints import all_blueprints


def create_app():
    """Flask application factory. Initializes and returns the Flask application.

    Blueprints are registered in here.

    :return:
    The initialized Flask application.
    """
    app = Flask(__name__)

    # Register blueprints.
    for bp in all_blueprints:
        logging.debug(u"Loading blueprint %s" % bp.import_name)
        import_module(bp.import_name)
        app.register_blueprint(bp)

    # Activate middleware.
    with app.app_context():
        logging.debug(u"Loading middleware tasks_app.middleware")
        import_module('tasks_app.middleware')

    # Return the application instance.
    return app
