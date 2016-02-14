###################################################################################################################
#
# F L A S K - R E S T F U L   A P I   B L U E P R I N T
#
# THIS IS THE ERROR HANDLING MODULE
#
###################################################################################################################

#
# IMPORTANT NOTE: This module, as-is, it's not extrictly necessary. It's only present in the development to show
#                 how to handle errors in this RESTful API.
#

from flask_restful import abort


def abort_if_not_exist(element, results, code, message):
    if element not in results:
         abort(code, message=message)
