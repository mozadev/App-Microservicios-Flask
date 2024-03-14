import os
from dotenv import load_dotenv
import dotenv

dotenv_file_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_file_path):
    load_dotenv(dotenv_file_path)
    
class Config:
    SQLALCHEMY_TRACK_MOFIFICATIONS = False
    
class DevelopmentConfig(Config):
    ENV = "development"
    
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://mozaco:Miloronegro1#@localhost:3306/dog"

class ProductionConfig(Config):
    pass





