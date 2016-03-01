###################################################################################################################
#
# S E L F C A R E   P A C K A G E   C O N F I G U R A T I O N
#
###################################################################################################################

from os import path


class Config:
    # General variables
    APP_DIR = path.abspath(path.dirname(__file__))
    STATIC_DIR = path.join(APP_DIR, 'static')
    IMAGES_DIR = path.join(STATIC_DIR, 'images')
    STYLES_DIR = path.join(STATIC_DIR, 'styles')
    TEMPLATE_DIR = path.join(APP_DIR, 'templates')
    # Related to API security
    USE_TOKEN_AUTH = True
    # Related to Flask-Restful API
    REST_URL_PREFIX = '/api'

    # Method with an application instance (for now, just a bypass)
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # Profile specific variables
    SECRET_KEY = '@_development_key_@'
    DEBUG = True
    # Related to Flask-Restful API testing
    DEBUG_TOOLBAR_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = True
    # Database connections comes here (in development)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(Config.APP_DIR, 'api.sqlite')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    # Profile specific variables
    SECRET_KEY = '$_testing_key_$'
    DEBUG = True
    TESTING = True
    # Related to Flask-Restful API testing
    DEBUG_TOOLBAR_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # Database connections comes here (in testing/QA)
    SQLALCHEMY_DATABASE_URI = 'mysql://superadm:superadm@192.168.69.155/brandmeister'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    # Profile specific variables
    SECRET_KEY = '%__Th1s1s4D4mnS1llyS3cr3tK3yF0rTh1s4ppl1c4t10n__B0FH_Ch4ng3It!__%'
    DEBUG = False
    # Related to Flask-Restful API testing
    DEBUG_TOOLBAR_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
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
