from flask import Blueprint

bp = Blueprint('errors', __name__)

from APP.errors import handlers
