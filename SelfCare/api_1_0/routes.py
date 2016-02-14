###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE ROUTES MODULE
#
###################################################################################################################
from . import api_version
from .resources.user import Users

api_version.add_resource(Users, '/users/<string:user>')
