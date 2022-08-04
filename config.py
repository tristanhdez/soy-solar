from os import environ, path
import os
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """BASE CONFIG"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = ''
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB= ''


class ProdConfig(Config):
    FLASK_DEBUG = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')


class StagingConfig(Config):
    FLASK_DEBUG = 'stating'
    DEVELOPMENT = True
    DEBUG = True


#export FLASK_DEBUG=development
class DevConfig(Config):
    FLASK_DEBUG = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')


class TestingConfig(Config):
    FLASK_DEBUG = 'testing'
    TESTING = True


configs = {
    "development": DevConfig,
    "production": ProdConfig,
    "stating": StagingConfig,
    "testing": TestingConfig
}
