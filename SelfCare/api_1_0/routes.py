###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE ROUTES MODULE
#
###################################################################################################################
from . import api_version
from .resources.users import User

api_version.add_resource(User, '/user/<string:user>')
