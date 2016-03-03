###################################################################################################################
#
# A P I   C O N F I G U R A T I O N
#
###################################################################################################################

from os import path
import redis


class Config:
    # General variables
    APP_DIR = path.abspath(path.dirname(__file__))
    # Related to API security and Tokens
    USE_TOKEN_AUTH = True

    # Enable rate limits only if redis is running
    try:
        r = redis.Redis()
        r.ping()
        USE_RATE_LIMITS = True
    except redis.ConnectionError:
        USE_RATE_LIMITS = False

    # Method with an application instance (for now, just a bypass)
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # Profile specific variables
    SECRET_KEY = '@_development_key_@'
    DEBUG = True
    # Database connections comes here (in development)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(Config.APP_DIR, 'api.sqlite')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    # Profile specific variables
    SECRET_KEY = '$_testing_key_$'
    DEBUG = True
    TESTING = True
    # Database connections comes here (in testing/QA)
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    # Profile specific variables
    SECRET_KEY = '%__Th1s1s4D4mnS1llyS3cr3tK3yF0rTh1s4ppl1c4t10n__B0FH_Ch4ng3It!__%'
    DEBUG = False
    # Database connections comes here (in production)
    SQLALCHEMY_DATABASE_URI = ''


# Finally, this is a dead simple configuration dictionary
config = {
    # Possible profiles to run under
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    # Default application profile
    'default': DevelopmentConfig
}

