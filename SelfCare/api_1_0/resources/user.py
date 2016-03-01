###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE USER MODULE
#
###################################################################################################################

from flask import jsonify
from flask_restful import Resource, reqparse
from ..common.errors import abort_if_not_exist

# With the following dictionrary we simulate a real database connection/query present or done at this point
dbQueryResult = {
    'user1': {'task': 'Build an API'},
    'user2': {'task': 'Coordinate development'},
    'user3': {'task': 'Develop core functionaliry'},
}

# With this function we parse the JSON-ified result from dbQuery
parser = reqparse.RequestParser()
parser.add_argument('task')


class UserAllMethods(Resource):
    def get(self):
        return jsonify(
            {'methods': [
                    {'get': 'http://127.0.0.1:5000/api/1.0/user/<string:username>'},
                    {'post': 'http://127.0.0.1:5000/api/1.0/user/<string:username>'},
                    {'delete': 'http://127.0.0.1:5000/api/1.0/user/<string:username>'},
                ]
            }
        )


class User(Resource):

    def get(self, user):
        abort_if_not_exist(user, dbQueryResult, 404, 'Sorry, the mentioned user ({}) does not exist')
        return dbQueryResult[user], 200

    def post(self, user):
        args = parser.parse_args()
        task = {'task': args['task']}
        dbQueryResult[user] = task
        return task, 201

    def delete(self, user):
        abort_if_not_exist(user, dbQueryResult, 404, 'Sorry, the mentioned user ({}) does not exist')
        del dbQueryResult[user]
        return '', 204

