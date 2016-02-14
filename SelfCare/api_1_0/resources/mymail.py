###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE MY MAIL MODULE
#
###################################################################################################################

from flask import jsonify
from flask_restful import Resource


class myMail(Resource):
    def get(self, user):
        # DB: Selects all email account related to an indicated username
        return jsonify({'message': '200 Query OK'})

    def put(self, user):
        # DB: Updates user’s password for an indicated username
        return jsonify({'message': '200 Updated OK'})

    def post(self, user):
        # DB: Creates a new email/password pair in DB for an indicated username
        return jsonify({'message': '200 Added OK'})

    def delete(self, user):
        # DB: Removes an email account from DB for an indicated username
        return jsonify({'message': '200 Removed OK'})
