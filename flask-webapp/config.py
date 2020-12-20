"""Flask config."""
from os import environ, path
import redis
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class BaseConfig:
    """Set Flask configuration vars from .env file"""

    # General Config
    FLASK_APP = environ.get('FLASK_APP')
    SECRET_KEY = environ.get('SECRET_KEY')

    LESS_BIN = environ.get('LESS_BIN')
    ASSETS_AUTO_BUILD = True

    #Flask-Session
    SESSION_TYPE = environ.get('SESSION_TYPE')
    SESSION_REDIS = redis.from_url(environ.get('SESSION_REDIS'))
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')

    # Database
    #SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    #SQLALCHEMY_ECHO = False
    #SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class ProdConfig(BaseConfig):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    #DATABASE_URI = environ.get('PROD_DATABASE_URI')
    ASSETS_DEBUG = False
    LESS_RUN_IN_DEBUG = False
    COMPRESSOR_DEBUG = False
    SQLALCHEMY_DATABASE_URI="postgres+psycopg2://postgres:postgres@192.168.248.130:5432/ramki_pirple"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_ENGINE_OPTIONS = {case_sensitive=True,echo=False}



#inherits BaseConfig
class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    ASSETS_DEBUG = True
    LESS_RUN_IN_DEBUG = True
    COMPRESSOR_DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgres+psycopg2://postgres:postgres@192.168.248.130:5432/ramki_pirple"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_ENGINE_OPTIONS = {case_sensitive=True,echo=False}
