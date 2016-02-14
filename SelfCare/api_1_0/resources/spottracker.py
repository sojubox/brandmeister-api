###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE SPOT TRACKER MODULE
#
###################################################################################################################

from flask import jsonify
from flask_restful import Resource


class spotTracker(Resource):
	def get(self, user):
		# DB: Selects all subscribed spot trackers for an indicated username
		return jsonify({'message': '200 Query OK'})

	def put(self, user):
		# DB: Updates one of the subscribed spot trackers for an indicated username
		return jsonify({'message': '200 Updated OK'})

	def delete(self, user):
		# DB: Removes one of the spot trackers subscribed for an indicated username
		return jsonify({'message': '200 Removed OK'})
