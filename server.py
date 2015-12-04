from gevent import monkey
monkey.patch_all()

from flask import Flask
from flask import render_template
from gevent.wsgi import WSGIServer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html', name = 'ddd')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0',debug = True)

app.debug = True
http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
