###################################################################################################################
#
# A P I   B L U E P R I N T
#
# THIS IS THE BUSINESS LOGIC BLUEPRINT PACKAGED
#
###################################################################################################################

from flask import Blueprint, g, url_for
from ..auth import auth
from ..decorators import rate_limit
from ..errors import ValidationError, bad_request

api = Blueprint('api', __name__)


# This function will present a JSON showing endpoints accessible via API
def get_catalog():
    return {
        'callsigns_url': url_for('api.get_callsigns', _external=True)
        }


# Basic error handling
@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(str(e))


# Basic HTTP error handling - Error 400 Bad Request
@api.errorhandler(400)
def bad_request_error(e):
    return bad_request('invalid request')


# Basic Rate-Limiting. A before_request is called to force Rate-Limit from now onwards
@api.before_request
@auth.login_required
@rate_limit(limit=5, period=15)
def before_request():
    pass


# Here we take care of HTTP headers after all internal processing and before send a response to the client
@api.after_request
def after_request(response):
    if hasattr(g, 'headers'):
        response.headers.extend(g.headers)
    return response


# We do this import sentence here at the end of the file in order TO AVOID CIRCULAR DEPENDENCIES IN FLASK
# DO NOT PAY ATTENTION TO THIS FACT
from api.v_1_0.SelfCare import callsigns



