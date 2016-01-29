import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '%__Th1s1s4D4mnS1llyS3cr3tK3yF0rTh1s4ppl1c4t10n__B0FH_Ch4ng3It!__%'

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

    # Default application profile to run under
    'default': DevelopmentConfig
}

