# Database models for this package will come here as necessary
#
# SELECT
# 	Users.ID, Users.Repeater, Users.Capabilities, Users.SSID, Users.Symbol, Users.Text, Users.Language, Users.Interval,
# 	Tunnels.Protocol, Tunnels.Network, Tunnels.Address, Tunnels.Firewall
# FROM Users
# LEFT JOIN Tunnels
# ON (Users.ID = Tunnels.ID)
# WHERE Users.Call = "ea1het"
# ORDER BY Priority
#
#

from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    __tablename__ = 'tb_AuthUsers'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(160))

    def __repr__(self):
        return '<User %r' % self.username


