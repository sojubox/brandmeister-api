import os


class Config:
    # Development's secret key
    SECRET_KEY = '%__Th1s1s4D4mnS1llyS3cr3tK3yF0rTh1s4ppl1c4t10n__B0FH_Ch4ng3It!__%'

    # Directory configuration
    APP_DIR = os.path.abspath(os.path.realpath(__file__))
    STATIC_DIR = os.path.join(APP_DIR, 'static')
    IMAGES_DIR = os.path.join(STATIC_DIR, 'images')

    # Method with an application instance (for now just a bypass)
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # Database connections comes here (development)


class ProductionConfig(Config):
    DEBUG = False
    # Database connections comes here (production)


config = {
    # This is a dead simple configuration dictionary

    # Possible profiles to run under
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    # Default application profile
    'default': DevelopmentConfig
}

