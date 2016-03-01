###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE ROUTES MODULE
#
###################################################################################################################
from . import api_version
from .resources.index import IndexNoAuth, IndexAuth
from .resources.call import Call
from .resources.dmrregistry import dmrRegistry
from .resources.mymail import myMail
from .resources.node import Node
from .resources.pushservice import pushService
from .resources.regpager import regPager
from .resources.spottracker import spotTracker
from .resources.user import User, UserAllMethods

api_version.add_resource(IndexNoAuth,   '/')
api_version.add_resource(IndexAuth,     '/get-token')

api_version.add_resource(Call,          '/call/<string:user>')
api_version.add_resource(dmrRegistry,   '/dreg/<string:user>')
api_version.add_resource(myMail,        '/mail/<string:user>')
api_version.add_resource(Node,          '/node/<string:user>')
api_version.add_resource(pushService,   '/psvc/<string:user>')
api_version.add_resource(regPager,      '/regp/<string:user>')
api_version.add_resource(spotTracker,   '/spot/<string:user>')


# User module is not necessary in this API but it illustrates how it should work
api_version.add_resource(UserAllMethods,'/user', '/user/')
api_version.add_resource(User,          '/user/<string:user>')
