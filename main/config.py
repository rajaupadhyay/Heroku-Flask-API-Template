import os

class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False  

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

class ProductionConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

config = {
    "default": "main.config.BaseConfig",
    "development": "main.config.DevelopmentConfig",
    "production": "main.config.ProductionConfig",
}

def configure_app(app):
    config_name= "production"
    app.config.from_object(config[config_name])