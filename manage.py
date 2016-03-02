###################################################################################################################
#
# B R A N D M E I S T E R ' S   R E S T F U L   A P I
#
# Developed by: Jonathan Gonzalez (EA1HET)
# Email: ea1het@ea1het.com
# Date: February/March 2016
#
# Mention: This API has been developed following concepts showed by Miguel Grinberg at PyCon 2015
# License: MIT (https://opensource.org/licenses/MIT)
#
# Project URL: http://brandmeister.network
#
###################################################################################################################

from api.app import create_app
from api.v_1_0.models import db, ApiUserAuth
from flask.ext.script import Manager

app = create_app('default')
manager = Manager(app)


# Register a new user from the CLI to start working with API
@manager.command
def add_apiuser(username):
    from getpass import getpass
    password = getpass()
    password2 = getpass(prompt='Confirm: ')
    if password != password2:
        import sys
        sys.exit('Error: passwords do not match.')
    db.create_all()
    user = ApiUserAuth(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    print('User {0} was registered successfully.'.format(username))


if __name__ == '__main__':
    manager.run()
