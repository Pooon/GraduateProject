from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html', name = 'ddd')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)
