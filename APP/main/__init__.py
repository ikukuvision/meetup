from flask import Blueprint

bp = Blueprint('main', __name__)

from APP.main import routes
