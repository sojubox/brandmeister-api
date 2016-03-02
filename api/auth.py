###################################################################################################################
#
# A P I   M O D U L E
#
# THIS IS THE DECORATORS MODULE
#
###################################################################################################################

from api.v_1_0.models import ApiUserAuth
from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from .errors import unauthorized

auth = HTTPBasicAuth()


# Here we try to verify a user with token or with user/pass pair. Token switch is evaluated at this point.
@auth.verify_password
def verify_password(username_or_token, password):
    if current_app.config['USE_TOKEN_AUTH']:
        # token authentication
        g.user = ApiUserAuth.verify_auth_token(username_or_token)
        return g.user is not None
    else:
        # username/password authentication
        g.user = ApiUserAuth.query.filter_by(username=username_or_token).first()
        return g.user is not None and g.user.verify_password(password)


# Basic error handler for unauthorized requests
@auth.error_handler
def unauthorized_error():
    return unauthorized()
