import os


class Config:
    # General options
    APP_DIR = os.path.abspath(os.path.realpath(__file__))
    STATIC_DIR = os.path.join(APP_DIR, 'static')
    IMAGES_DIR = os.path.join(STATIC_DIR, 'images')
    STYLES_DIR = os.path.join(STATIC_DIR, 'styles')
    TEMPLATE_DIR = os.path.join(STATIC_DIR, 'templates')

    # Related to Flask-Restful API
    REST_URL_PREFIX = '/api'

    # Related to databases
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MYDB_HOST = '127.0.0.1'
    MYDB_DATA = 'default_db'
    MYDB_USER = 'default_user'
    MYDB_PASS = 'password'

    # Method with an application instance (for now, just a bypass)
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SECRET_KEY = '%__Th1s1s4D4mnS1llyS3cr3tK3yF0rTh1s4ppl1c4t10n__B0FH_Ch4ng3It!__%'
    DEBUG = True
     # Related to Flask-Restful API testing
    DEBUG_TOOLBAR_ENABLED = True
    # MYDB_PORT = 5000
    # MYDB_HOST = '127.0.0.1'
    # Database connections comes here (in development)
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    # 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class TestingConfig(Config):
    SECRET_KEY = '%__Th1s1s4D4mnS1llyS3cr3tK3yF0rTh1s4ppl1c4t10n__B0FH_Ch4ng3It!__%'
    DEBUG = True
    # Related to Flask-Restful API testing
    DEBUG_TOOLBAR_ENABLED = True
    # MYDB_PORT = 5000
    # MYDB_HOST = '127.0.0.1'
    # Database connections comes here (in testing QA)
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    # 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SECRET_KEY = '%__Th1s1s4D4mnS1llyS3cr3tK3yF0rTh1s4ppl1c4t10n__B0FH_Ch4ng3It!__%'
    DEBUG = False
    # Related to Flask-Restful API testing
    DEBUG_TOOLBAR_ENABLED = True
    # MYDB_PORT = 5000
    # MYDB_HOST = '127.0.0.1'
    # Database connections comes here (in production)
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    # 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


# Finally, this is a dead simple configuration dictionary
config = {
    # Possible profiles to run under
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    # Default application profile
    'default': DevelopmentConfig
}

