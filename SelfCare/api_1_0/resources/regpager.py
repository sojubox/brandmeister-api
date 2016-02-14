###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE REGISTERED PAGERS (PAGE EXPRESS) MODULE
#
###################################################################################################################

from flask import jsonify
from flask_restful import Resource


class regPager(Resource):
    def get(self, user):
        # elects all registered pagers for an indicated username
        return jsonify({'message': '200 Query OK'})


    def put(self, user):
        # Updates on of the user’s pagers for an indicated username
        return jsonify({'message': '200 Updated OK'})
