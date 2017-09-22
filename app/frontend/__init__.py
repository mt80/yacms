from flask import Blueprint

frontend = Blueprint('frontend', __name__, template_folder='templates', static_folder='static/public',
                     static_url_path='')

from app.frontend.routes import index
from app.frontend.routes import articles
