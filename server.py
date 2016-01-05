from gevent import monkey
monkey.patch_all()

from GraduateProject import app, db
from gevent.wsgi import WSGIServer
from GraduateProject.config import SERVER, PORT
from GraduateProject.model.user import User
from flask.ext.script import Shell, Manager

manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    app.debug = True
    #manager.run() #!use this only in case that python shell environ' is needed
    http_server = WSGIServer((SERVER, PORT), app)
    http_server.serve_forever()
    




