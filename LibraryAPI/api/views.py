from flask import request
from LibraryAPI.utils import add_generic_endpoints

from . import api

add_generic_endpoints(api)
