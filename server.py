from gevent import monkey
monkey.patch_all()

from GraduateProject import app
from gevent.wsgi import WSGIServer
# from GraduateProject.config import SERVER, PORT

if __name__ == '__main__':
    app.debug = True
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()

