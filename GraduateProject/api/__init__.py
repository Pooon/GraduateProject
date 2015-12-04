from flask import render_template
from GraduateProject import app

@app.route('/')
def index():
    return render_template('/hello.html', name = '6666666')

import user