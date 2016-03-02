###################################################################################################################
#
# A P I   B L U E P R I N T
#
# THIS IS THE TOKEN GENERATION BLUEPRINT
#
###################################################################################################################

from api.v_1_0.models import ApiUserAuth
from flask import Blueprint, g
from flask_httpauth import HTTPBasicAuth
from .decorators import json
from .errors import unauthorized

token = Blueprint('token', __name__)
token_auth = HTTPBasicAuth()


# This block allows to verify a password
@token_auth.verify_password
def verify_password(username, password):
    g.user = ApiUserAuth.query.filter_by(username=username).first()
    if not g.user:
        return False
    return g.user.verify_password(password)


# Basic error message when the client first arrives
@token_auth.error_handler
def unauthorized_error():
    return unauthorized('Please authenticate to get your token.')


# This is the endpoint a client must call and the method that must be used to grab a token via API
@token.route('/request-token', methods=['POST'])
@token_auth.login_required
@json
def request_token():
    # Note that a colon is appended to the token. When the token is sent in the authorization header this will put the
    # token in the username field and an empty string in the password field.
    return {'token': g.user.generate_auth_token() + ':'}
