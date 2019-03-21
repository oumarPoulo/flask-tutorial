#!/usr/bin/python -W ignore
# coding: utf8

import logging

from flask import jsonify
from flask_swagger import swagger
from tasks_app.application import create_app

# Create a flask instance app
app = create_app()


# Swagger spec definition
@app.route('/spec')
def spec():
    swag = swagger(app, from_file_keyword='swagger_from_file')
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Tasks Provider API"
    return jsonify(swag)


if __name__ == '__main__':
    logging.debug("***************************************************")
    logging.debug("starting flask api")
    logging.debug("***************************************************")
    app.run()
