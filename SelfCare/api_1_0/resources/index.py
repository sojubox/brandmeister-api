###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE INDEX MODULE
#
###################################################################################################################

from flask import jsonify, request, abort, url_for, current_app, make_response, g
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from ...config import Config
from ...api_1_0 import API_VERSION


class IndexNoAuth(Resource):
    def get(self):
        response = jsonify({'status': '401','message': 'Unauthorized'})
        response.status_code = 401
        response.headers['Location'] = '%s/%s/get-token' % (Config.REST_URL_PREFIX, API_VERSION)
        return response


class IndexAuth(Resource):
    def get(self):
        response = jsonify({'status': '405', 'message': 'Method not allowed'})
        response.status_code = 405
        return response

    def post(self):
        # Here we authenticate a user and generate a token
        username = request.json.get('username')
        password = request.json.get('password')

        # Here we check for missing arguments in JSON
        if username is None or password is None:
            response = jsonify({'status': '400', 'message': 'Syntax error'})
            response.status_code = 400
            return response
        if len(username) == 0:
            response = jsonify({'status': '404', 'message': 'Not found. An element was expected (username).'})
            response.status_code = 404
            return response
        if len(password) == 0:
            response = jsonify({'status': '404', 'message': 'Not found. An element was expected (password).'})
            response.status_code = 404
            return response
        if not request.json:
            response = jsonify({'status': '400', 'message': 'Syntax error'})
            response.status_code = 400
            return response

        # Here we generate a token based on the password
        token = generate_password_hash(password)

        # Here we send a response in JSON format
        response = jsonify({'status': '200', 'message': 'Authenticated', 'token': token})
        response.status_code = 200
        return response

