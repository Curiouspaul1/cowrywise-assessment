from flask import request, current_app

from . import users_bp
from schemas.User import UserSchema
from LibraryAPI.api.messages import (
    INVALID_DATA_FORMAT,
    ADDED_NEW_USER
)
from extensions import Session
from LibraryAPI.utils import AppResponse


@users_bp.post('/')
def add_new_user():
    body = request.get_json(force=True)
    resp = AppResponse()

    try:
        with Session.begin() as sess:
            schema = UserSchema()
            new_user = schema.load(body)
            sess.add(new_user)

            res = schema.dump(new_user)
        return resp.success(
            data=schema.dump(res),
            message=ADDED_NEW_USER
        )
    except Exception as e:
        print(str(e))
        return resp.error(message=INVALID_DATA_FORMAT)
