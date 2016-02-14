###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE USER MODULE
#
###################################################################################################################

from flask_restful import Resource, reqparse, abort
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
