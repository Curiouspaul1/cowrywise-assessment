from flask import request
from utils import add_generic_endpoints
from .utils import sync_actions

from . import api

add_generic_endpoints(api)


@api.post('/wbhook')
def db_action_webhook():
    """
        An improvement would be to use uuids to make sure of
        consistency across both services.
    """
    data = request.get_json()
    action = data['action']

    sync_actions[action](data)

    return {
        'status': 'success'
    }, 200
