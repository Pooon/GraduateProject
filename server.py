from gevent import monkey
monkey.patch_all()

from GraduateProject import app, db
from gevent.wsgi import WSGIServer
from GraduateProject.config import SERVER, PORT
from flask.ext.script import Shell, Manager

from GraduateProject.model.user import User
from GraduateProject.model.category import Category
from GraduateProject.model.course import Course
from GraduateProject.model.lecture import Lecture

manager = Manager(app)

@manager.command
def createall():
    "Creates database tables"

    db.create_all()

def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    app.debug = True
    # manager.run() #!use this only in case that python shell environ' is needed
    http_server = WSGIServer((SERVER, PORT), app)
    http_server.serve_forever()
    




