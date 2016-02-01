from appkg_SelfCare import create_app
from flask.ext.script import Manager, Server

# The following two steps can easily be done with just one sentence, but for the sake of understanding I'm going to
# create an application factory app and later I'm going to create a manager that will take care of that app (theApp).

# So, 1st, we define the type of application we are going to launch, or set the default if nothing valid is specified.
theApp = create_app('development' or 'default')

# And 2nd, we launch the newly created app under the configuration scheme required.
manager = Manager(theApp)
manager.add_command("runserver", Server(host="0.0.0.0", port=5000))

# Finally, we launch the application using the manager instance. Here we control the running parameters like the
# address we are going to bind, TCP port to be used and many other features.

if __name__ == '__main__':
    manager.run()
