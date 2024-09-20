from flask import (
    request,
    current_app
)
from sqlalchemy import select

from . import users_bp
from schemas import (
    UserSchema,
    UserBorrowsSchema
)
from core.api.messages import (
    INVALID_DATA_FORMAT
)
from models import User
from extensions import Session
from utils import AppResponse


@users_bp.get('/')
def fetch_users():
    if 'borrows' in request.args:
        schema = UserBorrowsSchema(many=True)
    else:
        schema = UserSchema(many=True)

    if 'page' in request.args:
        page = request.args.get('page')
    else:
        page = 1
    PER_PAGE = current_app.config['PAGINATION_LIMIT']

    with Session() as sess:
        stmt = select(User)
        all_users = stmt.offset(page).limit(PER_PAGE)
        all_users = sess.scalars(stmt)
        all_users = schema.dump(all_users)

    return AppResponse().success(
        data=all_users
    )
