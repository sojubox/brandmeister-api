###################################################################################################################
#
# A P I   M O D U L E
#
# THIS IS A BUSINESS LOGIC MODULE
#
###################################################################################################################

from api.decorators import json, etag, collection
from api.v_1_0 import api
from api.v_1_0.models import db, Callsign
from flask import request


@api.route('/callsigns/', methods=['GET'])
@etag
@json
@collection(Callsign)
def get_callsigns():
    return Callsign.query


@api.route('/callsigns/<string:callsign>', methods=['GET'])
@etag
@json
def get_callsign(callsign):
    return Callsign.query.get_or_404(callsign)


@api.route('/callsigns/', methods=['POST'])
@json
def new_callsign():
    callsign = Callsign().import_data(request.get_json(force=True))
    db.session.add(callsign)
    db.session.commit()
    return {}, 201, {'Location': callsign.get_url()}


@api.route('/callsigns/<string:callsign>', methods=['PUT'])
@json
def edit_callsign(callsign):
    callsign = Callsign.query.get_or_404(callsign)
    callsign.import_data(request.get_json(force=True))
    db.session.add(callsign)
    db.session.commit()
    return {}


@api.route('/callsigns/<string:callsign>', methods=['DELETE'])
@json
def delete_callsign(callsign):
    callsign = Callsign.query.get_or_404(callsign)
    db.session.delete(callsign)
    db.session.commit()
    return {}
