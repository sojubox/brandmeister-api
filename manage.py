from appkg_SelfCare import create_app
from flask.ext.script import Manager

app = create_app('development' or 'default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
