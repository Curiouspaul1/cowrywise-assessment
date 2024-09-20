from flask import request

from . import users_bp
from schemas.User import UserSchema
from core.api.messages import (
    INVALID_DATA_FORMAT,
    ADDED_NEW_USER
)
from extensions import Session
from utils import AppResponse


@users_bp.post('/')
def add_new_user():
    body = request.get_json(force=True)
    resp = AppResponse()
    schema = UserSchema()

    try:
        with Session() as sess:
            new_user = schema.load(body)
            sess.add(new_user)
            sess.commit()
            res = schema.dump(new_user)
        return resp.success(
            data=res,
            message=ADDED_NEW_USER
        )
    except Exception as e:
        raise e
        return resp.error(
            data=str(e),
            message=INVALID_DATA_FORMAT
        )
