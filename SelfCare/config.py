###################################################################################################################
#
# S E L F C A R E   P A C K A G E   C O N F I G U R A T I O N
#
###################################################################################################################

from os import path


class Config:
    # Genral variables
    APP_DIR = path.abspath(path.dirname(__file__))
    STATIC_DIR = path.join(APP_DIR, 'static')
    IMAGES_DIR = path.join(STATIC_DIR, 'images')
    STYLES_DIR = path.join(STATIC_DIR, 'styles')
    TEMPLATE_DIR = path.join(APP_DIR, 'templates')
    # Related to Flask-Restful API
    REST_URL_PREFIX = '/api'
    # Related to databases
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


    # Method with an application instance (for now, just a bypass)
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # Profile specific variables
    SECRET_KEY = '@_development_key_@'
    DEBUG = True
     # Related to Flask-Restful API testing
    DEBUG_TOOLBAR_ENABLED = True
    # Database connections comes here (in development)
    # MYDB_HOST = '127.0.0.1'
    # MYDB_PORT = 3306
    # MYDB_DATA = 'db_development'
    # MYDB_USER = 'username'
    # MYDB_PASS = 'password'


class TestingConfig(Config):
    # Profile specific variables
    SECRET_KEY = '$_testing_key_$'
    DEBUG = True
    # Related to Flask-Restful API testing
    DEBUG_TOOLBAR_ENABLED = True
    # Database connections comes here (in testing QA)
    # MYDB_HOST = '127.0.0.1'
    # MYDB_PORT = 3306
    # MYDB_DATA = 'db_testing'
    # MYDB_USER = 'username'
    # MYDB_PASS = 'password'


class ProductionConfig(Config):
    # Profile specific variables
    SECRET_KEY = '%__Th1s1s4D4mnS1llyS3cr3tK3yF0rTh1s4ppl1c4t10n__B0FH_Ch4ng3It!__%'
    DEBUG = False
    # Related to Flask-Restful API testing
    DEBUG_TOOLBAR_ENABLED = True
    # Database connections comes here (in production)
    # MYDB_HOST = '127.0.0.1'
    # MYDB_PORT = 3306
    # MYDB_DATA = 'db_production'
    # MYDB_USER = 'username'
    # MYDB_PASS = 'password'


# Finally, this is a dead simple configuration dictionary
config = {
    # Possible profiles to run under
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    # Default application profile
    'default': DevelopmentConfig
}
