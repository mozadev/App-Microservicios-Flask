import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app= Flask(__name__)
    CORS(app)
    
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    
    app.config.from_object(environment_configuration)
    
    db.init_app(app)
    
    with app.app_context():
        #Register blueprint
        from .dog_api import dog_api_blueprint
        app.register_blueprint(dog_api_blueprint)
        return app