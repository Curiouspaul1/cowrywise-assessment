import os
from typing import Union

import requests
from flask import (
    Flask, Blueprint, jsonify
)
from dotenv import load_dotenv

load_dotenv()


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


def send_request(url_path, payload, headers={}, form_data=False):
    API_DOMAIN = os.getenv('LibraryService')
    print(API_DOMAIN)
    if form_data:
        post = requests.post(
            url=f"http://{API_DOMAIN}/{url_path}",
            data=payload,
            headers=headers
        )
    else:
        post = requests.post(
            url=f"http://{API_DOMAIN}/{url_path}",
            json=payload,
            headers=headers
        )
    if not post.status_code == 200:
        print("An error occurred while sending request to LibraryService")
        raise Exception(str(post.text))
    return post.json()
