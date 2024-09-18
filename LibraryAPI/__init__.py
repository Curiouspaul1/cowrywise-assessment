from flask import Flask

from extensions import init_ext
from .utils import add_generic_endpoints
from config import config_options


def create_app(config_name='default'):
    app = Flask(__name__)

    # add config
    app.config.from_object(config_options[config_name])

    # init extensions if any
    init_ext(app)

    # register blueprints
    from .api import api
    app.register_blueprint(api)

    # generic endpoints
    add_generic_endpoints(app)

    return app
