from typing import Union
from flask import (
    Flask, Blueprint, jsonify
)


def add_generic_endpoints(
    app: Union[None, Flask, Blueprint],
    custom_index_message=None
):
    # generic endpoints
    @app.get('/ping')
    def app_status():
        return 'ok', 200

    @app.get('/')
    def index():
        message = "The Cowrywise App is Online"
        if custom_index_message:
            message = custom_index_message
        return f"""
            <h1> {message} </h1>
        """

    # register errror handler
    @app.errorhandler(404)
    def not_found(error):
        return 'Page/Resource not found', 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify(
            {
                'status': 'failed',
                'data': None,
                'message': str(error)
            }
        ), 500


class AppResponse:
    def success(self, data=None, message=None):
        return jsonify(
            {
                'status': 'success',
                'data': data,
                'message': message
            }
        ), 200

    def error(self, error_code=400, message=None, data=None):
        return jsonify(
            {
                'status': 'error',
                'data': data,
                'message': message
            }
        ), error_code
