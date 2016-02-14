###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE CALL(SIGN) MODULE
#
###################################################################################################################

from flask import jsonify
from flask_restful import Resource


class Call(Resource):
    def get(self, user):
        # DB: Selects user’s profile from DB for an indicated username
        return jsonify({'message': '200 Query OK' })


    def post(self, user):
        # DB: Updates user’s profile in DB for an indicated username
        return jsonify({'message': '200 Updated OK'})
