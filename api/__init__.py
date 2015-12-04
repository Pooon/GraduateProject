from server import app
from flask import render_template

@app.route('/')
def index():
    return render_template('/hello.html', name = '6666666')


import user