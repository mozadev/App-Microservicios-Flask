from flask import Blueprint

dog_api_blueprint = Blueprint('dog_api', __name__)  

from . import routes

