from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')


# register "sub" blueprints
from .books import books_bp  # noqa: E402
from .users import users_bp  # noqa: E402

api.register_blueprint(books_bp)
api.register_blueprint(users_bp)

from . import views  # noqa: F401 E402
