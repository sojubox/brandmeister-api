from flask import Flask, render_template
from datetime import datetime
from flask.ext.moment import Moment
from config import config
from appkg_SelfCare import main, api_1_0


# Moment initialization
moment = Moment()


# Application factory: create_app initialization
# This code can be called several times later on-demand
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)

    # The config_name variable will be filled with either Production or Development parameters from config.py
    # After application initialization here comes all application routes and custom decorators

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/apidocs/')
    def apidocs():
        return render_template('apidocs.html')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors.html', currentTime=datetime.utcnow(),
                               errorNumber=e, errorLiteral='Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors.html', currentTime=datetime.utcnow(),
                               errorNumber=e, errorLiteral='Internal Server Error'), 500

    # An application will be run
    return app
