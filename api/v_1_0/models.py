###################################################################################################################
#
# A P I   M O D E L S
#
# THIS IS THE DATABASE MODEL DEFINITION
#
###################################################################################################################

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import NotFound
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from api.helpers import args_from_url
from api.errors import ValidationError

db = SQLAlchemy()


class Callsign(db.Model):
    __tablename__ = 'callsigns'
    callsign = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), index=True)

    def get_url(self):
        return url_for('api.get_callsign', callsign=self.callsign, _external=True)

    def export_data(self):
        return {'self_url': self.get_url(),
                'name': self.name,
                'callsign': self.callsign
                }

    def import_data(self, data):
        try:
            self.callsign = data['callsign']
            self.name = data['name']
        except KeyError as e:
            raise ValidationError('Invalid callsign: missing ' + e.args[0])
        return self


# This model is defined to validate users that connect to the API
class ApiUserAuth(db.Model):
    __tablename__ = 'api_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return ApiUserAuth.query.get(data['id'])

