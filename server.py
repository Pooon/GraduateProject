from gevent import monkey
monkey.patch_all()

from flask import Flask
from gevent.wsgi import WSGIServer
from config import SERVER, PORT

app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    http_server = WSGIServer((SERVER, PORT), app)
    http_server.serve_forever()

