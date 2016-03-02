###################################################################################################################
#
# A P I   M O D U L E
#
# THIS IS THE ERRORS MODULE
#
###################################################################################################################

from flask import jsonify, url_for, current_app


class ValidationError(ValueError):
    pass


# HTTP Error 304 - Not Modified
def not_modified():
    response = jsonify({'status': 304, 'error': 'not modified'})
    response.status_code = 304
    return response


# HTTP Error 400 - Bad Request
def bad_request(message):
    response = jsonify({'status': 400, 'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


# HTTP Error 401 - Unauthorized
def unauthorized(message=None):
    if message is None:
        if current_app.config['USE_TOKEN_AUTH']:
            message = 'Please authenticate with your token.'
        else:
            message = 'Please authenticate.'
    response = jsonify({'status': 401, 'error': 'unauthorized', 'message': message})
    response.status_code = 401
    if current_app.config['USE_TOKEN_AUTH']:
        response.headers['Location'] = url_for('token.request_token')
    return response


# HTTP Error 404 - Not Found
def not_found(message):
    response = jsonify({'status': 404, 'error': 'not found',
                        'message': message})
    response.status_code = 404
    return response


# HTTP Error 405 - Method not allowed
def not_allowed():
    response = jsonify({'status': 405, 'error': 'method not allowed'})
    response.status_code = 405
    return response


# HTTP Error 412 - Precondition failed
def precondition_failed():
    response = jsonify({'status': 412, 'error': 'precondition failed'})
    response.status_code = 412
    return response


# HTTP Error 429 - Too many requests (Rate limit exceeded)
def too_many_requests(message='You have exceeded your request rate'):
    response = jsonify({'status': 429, 'error': 'too many requests', 'message': message})
    response.status_code = 429
    return response
