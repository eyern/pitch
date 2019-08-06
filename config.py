import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://iankipkoech@localhost/pitchapp'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # e-mail configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") 
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production config child class

    Args:
        Config: The parent config class with general config classes
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Testing config child class

    Args:
        Config: The parent config class with General config settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://iankipkoech:koech150@localhost/pitchapp'

class DevConfig(Config):
    '''
    Dev config child class

    Args:
        Config: The parent config class with general config settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://iankipkoech:koech150@localhost/pitchapp'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

