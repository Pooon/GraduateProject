from flask import render_template
from GraduateProject import app

@app.route('/')
def getHompage():
	
	return render_template('hello.html', name = 'linqitao')