###################################################################################################################
#
# A P I   M A I N   A P P L I C A T I O N
#
# THIS IS THE APPLICATION FACTORY
#
###################################################################################################################

from config import config
from api.v_1_0.models import db
from flask import Flask
from .auth import auth
from .decorators import json, etag
from .errors import not_found, not_allowed


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    ###############################################################################################################
    #
    # F L A S K   I N I T I A L I Z A T I O N S
    #
    ###############################################################################################################

    # Here we connect to the database defined in the model specified at the import above (via SQLAlchemy)
    db.init_app(app)

    ###############################################################################################################
    #
    # F L A S K   B L U E P R I N T S   W I T H   T H E I R   O W N   R O U T E S   A N D   D E C O R A T O R S
    #
    ###############################################################################################################

    from api.v_1_0 import api as api_bp
    app.register_blueprint(api_bp, url_prefix='/1.0')

    # This is a switch to enable or disable token usage
    if app.config['USE_TOKEN_AUTH']:
        from api.token import token as token_bp
        app.register_blueprint(token_bp, url_prefix='/auth')

    @app.route('/')
    @auth.login_required
    @etag
    @json
    def index():
        from api.v_1_0 import get_catalog as v1_0_catalog
        return {
            'versions': {'1.0': v1_0_catalog()}
        }

    @app.errorhandler(404)
    @auth.login_required
    def not_found_error(e):
        return not_found('item not found')

    @app.errorhandler(405)
    def method_not_allowed_error(e):
        return not_allowed()

    return app
