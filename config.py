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
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'Password123*'
    MYSQL_DATABASE_DB= 'solar'
    
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT= 465
    MAIL_USERNAME = 'solarbotsupp@gmail.com'
    MAIL_PASSWORD = 'rljfpaheyxwmroop'
    #MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    #CSRF_ENABLED = True
    #SESSION_COOKIE_SECURE=True
    #SESSION_COOKIE_HTTPONLY=True
    #SESSION_COOKIE_SAMESITE='Lax'


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')

class StagingConfig(Config):
    FLASK_ENV = 'stating'
    DEVELOPMENT = True
    DEBUG = True

#export FLASK_ENV=development
class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True

configs = {
    "development": DevConfig, 
    "production": ProdConfig, 
    "stating":StagingConfig,
    "testing":TestingConfig
}