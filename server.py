from gevent import monkey
monkey.patch_all()

from flask import Flask
from flask import render_template
from gevent.wsgi import WSGIServer
from config import SERVER, PORT

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html', name = 'ddd')

if __name__ == '__main__':
    app.debug = True
    http_server = WSGIServer((SERVER, PORT), app)
    http_server.serve_forever()
