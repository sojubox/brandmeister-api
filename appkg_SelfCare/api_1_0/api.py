from flask import Flask, jsonify

@app.route('/api/v1.0/call/<username>’, methods = [‘GET’])
def getCall():
	# Selects user’s profile from DB for an indicated username
	# return jsonify({ ‘message’: “200 Query OK” })
	pass


@app.route('/api/v1.0/call/<username>’, methods = [‘PUT’])
def putCall():
	# Updates user’s profile in DB for an indicated username
	# return jsonify({ ‘message’: “200 Updated OK” })
	pass


@app.route('/api/v1.0/node/<username>’, methods = [‘GET’])
def getNodes():
	# Selects all registered modules for an indicated username
	# return jsonify({ ‘message’: “200 Query OK” })
	pass


@app.route('/api/v1.0/node/<username>’, methods = [‘PUT’])
def putNodes():
	# Updates one of the user’s registered module for an indicated username
	# return jsonify({ ‘message’: “200 Updated OK” })
	pass


@app.route('/api/v1.0/node/<username>’, methods = [‘POST’])
def postNodes():
	# Register a new module in database for an indicated username 
	# return jsonify({ ‘message’: “200 Added OK” })
	pass


@app.route('/api/v1.0/node/<username>’, methods = [‘DELETE’])
def deleNodes():
	# Deletes a registered module for an indicated username (currently not implemented)
	# return jsonify({ ‘message’: “200 Removed OK” })
	pass


@app.route('/api/v1.0/dmrreg/<username>’, methods = [‘GET’])
def getDRMRegistry():
	# Selects all information from DB for an indicated username
	# return jsonify({ ‘message’: “200 Query OK” })
	pass


@app.route('/api/v1.0/dmrreg/<username>’, methods = [‘PUT’])
def putDMRRegistry():
	# Updates all information into DB for an indicated username
	# return jsonify({ ‘message’: “200 Updated OK” })
	pass


@app.route('/api/v1.0/pushsvc/<username>’, methods = [‘GET’])
def getPushService():
	# Selects all subscribed notification receivers for an indicated username
	# return jsonify({ ‘message’: “200 Query OK” })
	pass


@app.route('/api/v1.0/pushsvc/<username>’, methods = [‘PUT’])
def putPushService():
	# Updates one of the user’s subscribed notification receivers for an indicated username
	# return jsonify({ ‘message’: “200 Updated OK” })
	pass


@app.route('/api/v1.0/regpag/<username>’, methods = [‘GET’])
def getRegPager():
	# Selects all registered pagers for an indicated username
	# return jsonify({ ‘message’: “200 Query OK” })
	pass


@app.route('/api/v1.0/regpag/<username>’, methods = [‘PUT’])
def putRegPager():
	# Updates on of the user’s pagers for an indicated username
	# return jsonify({ ‘message’: “200 Updated OK” })
	pass


@app.route('/api/v1.0/mymail/<username>’, methods = [‘GET’])
def getMyMail():
	# Selects all email account related to an indicated username
	# return jsonify({ ‘message’: “200 Query OK” })
	pass


@app.route('/api/v1.0/mymail/<username>’, methods = [‘PUT’])
def putMyMail():
	# Updates user’s password for an indicated username
	# return jsonify({ ‘message’: “200 Updated OK” })
	pass


@app.route('/api/v1.0/mymail/<username>’, methods = [‘POST’])
def postMyMail():
	# Creates a new email/password pair in DB for an indicated username
	# return jsonify({ ‘message’: “200 Added OK” })
	pass


@app.route('/api/v1.0/mymail/<username>’, methods = [‘DELETE’])
def deleMyMail():
	# Removes an email account from DB for an indicated username
	# return jsonify({ ‘message’: “200 Removed OK” })
	pass


@app.route('/api/v1.0/spottrk/<username>’, methods = [‘GET’])
def getSpotTracker():
	# Selects all subscribed spot trackers for an indicated username
	# return jsonify({ ‘message’: “200 Query OK” })
	pass


@app.route('/api/v1.0/spottrk/<username>’, methods = [‘PUT’])
def putSpotTracker():
	# Updates one of the subscribed spot trackers for an indicated username
	# return jsonify({ ‘message’: “200 Updated OK” })
	pass


@app.route('/api/v1.0/spottrk/<username>’, methods = [‘DELE’])
def deleSpotTracker():
	# Removes one of the spot trackers subscribed for an indicated username
	# return jsonify({ ‘message’: “200 Removed OK” })
	pass

