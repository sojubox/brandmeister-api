###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE (MY) NODES MODULE
#
###################################################################################################################

from flask import jsonify
from flask_restful import Resource


class Node(Resource):
    def get(self, user):
        # DB: Selects all registered modules for an indicated username
        return jsonify({'message': '200 Query OK'})

    def put(self, user):
        # DB: Updates one of the user’s registered module for an indicated username
        return jsonify({'message': '200 Updated OK'})

    def post(self, user):
        # DB: Register a new module in database for an indicated username
        return jsonify({'message': '200 Added OK'})

    def delete(self, user):
        # DB: Deletes a registered module for an indicated username (currently not implemented)
        return jsonify({'message': '200 Removed OK'})
