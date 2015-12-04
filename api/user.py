from api import app
from flask import jsonify, request

@app.route('/user',methods = ['POST'])
def user_login():

	return 'Hello World!'
