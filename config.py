import os

class Config(object):
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SECRET_KEY = os.getenv(key='SECRET_KEY', default='you-will-never-guess')
