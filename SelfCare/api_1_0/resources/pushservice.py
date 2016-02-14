###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE PUSH SERVICE (SUSCRIBED NOTIFICATION RECEIVERS) MODULE
#
###################################################################################################################

from flask import jsonify
from flask_restful import Resource


class pushService(Resource):
	def get(self, user):
		# Selects all subscribed notification receivers for an indicated username
		return jsonify({'message': '200 Query OK'})

	def put(self, user):
		# Updates one of the user’s subscribed notification receivers for an indicated username
		return jsonify({'message': '200 Updated OK'})
