###################################################################################################################
#
# S E L F C A R E   P A C K A G E
#
# THIS IS THE PACKAGE CONSTRUCTOR
#
###################################################################################################################

from SelfCare.config import config
from flask import Flask, render_template
from flask.ext.bcrypt import Bcrypt
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy

# Definition of elements to be used into the app that is going to be launched
moment = Moment()
db = SQLAlchemy()
flask_bcrypt = Bcrypt()


# Application factory
# This portion of code can be called several times
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialization of previously defined elements to be used into the app
    moment.init_app(app)
    db.init_app(app)
    flask_bcrypt.init_app(app)

    # The following import provides route inspection under development and testing environments
    try:
        from flask_debugtoolbar import DebugToolbarExtension
        DebugToolbarExtension(app)
    except:
        pass

    ###################################################################################################################
    #
    # G E N E R I C   A N D / O R   S T A T I C   A P P   R O U T E S
    #
    ###################################################################################################################

    # Attach routes and custom error pages here
    # @app.route('/')
    # def index():
    #     return render_template('index.html')
    #
    # @app.route('/apidocs/')
    # def apidocs():
    #     return render_template('apidocs.html')
    #
    # @app.errorhandler(404)
    # def page_not_found(e):
    #     return render_template('errors.html', currentTime=datetime.utcnow(),
    #                            errorNumber=e, errorLiteral='Not Found'), 404
    #
    # @app.errorhandler(500)
    # def internal_server_error(e):
    #     return render_template('errors.html', currentTime=datetime.utcnow(),
    #                           errorNumber=e, errorLiteral='Internal Server Error'), 500

    ###################################################################################################################
    #
    # F L A S K   B L U E P R I N T S   W I T H   T H E I R   O W N   R O U T E S
    #
    ###################################################################################################################

    from SelfCare.api_1_0 import api_bp, API_VERSION

    # Blueprint registration into main program
    app.register_blueprint(
        api_bp,
        url_prefix='{prefix}/{version}'.format(prefix=app.config['REST_URL_PREFIX'], version=API_VERSION)
    )

    # This clause brings blueprint's routes to main program at this point
    import SelfCare.api_1_0.routes

    # ----------------------------------------------------------------------------------------------------------------

    return app
