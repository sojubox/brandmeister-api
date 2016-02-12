###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE USERS MODULE
#
###################################################################################################################

from flask_restful import Resource, reqparse, abort

# With the following dictionrary we simulate a real database connection

USERS = {
    'user1': {'task': 'Build an API'},
    'user2': {'task': 'Coordinate development'},
    'user3': {'task': 'Build core'},
}

def abort_if_user_doesnt_exist(user):
    if user not in USERS:
         abort(404, message="Callsign {} doesn't exist".format(user))

parser = reqparse.RequestParser()
parser.add_argument('task')


class User(Resource):

    def get(self, user):
        abort_if_user_doesnt_exist(user)
        return USERS[user]

    def delete(self, user):
        abort_if_user_doesnt_exist(user)
        del USERS[user]
        return '', 204

    def put(self, user):
        args = parser.parse_args()
        task = {'task': args['task']}
        USERS[user] = task
        return task, 201
