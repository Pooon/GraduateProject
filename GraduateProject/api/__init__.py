from flask import render_template
from GraduateProject import app

@app.route('/')
def index():
    return 'Hello'

from .user import user