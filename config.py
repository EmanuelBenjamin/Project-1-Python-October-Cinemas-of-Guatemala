from decouple import config


class config:
    SECRET_KEY = config('SECRET_KEY')

class developmentConfig(config):
    DEBUG = True

config = {
    'development': developmentConfig
}