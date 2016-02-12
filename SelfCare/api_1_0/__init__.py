###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE PACKAGE/BLUEPRINT CONSTRUCTOR
#
###################################################################################################################

from flask import Blueprint
from flask_restful import Api


# This is the official version of this RESTful API blueprint
# This parameter affects API URL, so, THIS MUST BE CONFIGURED PROPERLY.
API_VERSION = 1.0


api_bp = Blueprint('api', __name__)
api_version = Api(api_bp)

# Note: If your IDE complains about the last line, please, do not pay attention to it (PyCharm 5).
