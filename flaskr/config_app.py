import os

DEFAULT_USER = os.environ.get('DATABASE_USER', 'postgres')
DEFAULT_PWD = os.environ.get('DATABASE_PASSWORD', '0')
DEFAULT_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DEFAULT_PORT = os.environ.get('DATABASE_PORT', '5432')

DEFAULT_DATABASE = os.environ.get('DEFAULT_DATABASE', 'jet_db')


DEFAULT_DB_SCHEMA = os.environ.get('DEFAULT_DB_SCHEMA', 'public')

DEFAULT_DATABASE_URL = os.environ.get(
    'DEFAULT_DATABASE_URL',
    f'postgresql://{DEFAULT_USER}:{DEFAULT_PWD}@{DEFAULT_HOST}:{DEFAULT_PORT}/{DEFAULT_DATABASE}'
)

SQLALCHEMY_TRACK_MODIFICATIONS = int(os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', '0')) == 1
SQLALCHEMY_ECHO = int(os.environ.get('SQLALCHEMY_ECHO', '0')) == 1
FLASK_DEBUG = int(os.environ.get('FLASK_DEBUG', '0')) == 1

SECRET_KEY = os.environ.get('SECRET_KEY', 'my-secret-key')

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', '6379'))
REDIS_PWD = os.environ.get('REDIS_PWD', 'redis')
REDIS_EXPIRATION_TIME = int(os.environ.get('REDIS_EXPIRATION_TIME', '3600'))