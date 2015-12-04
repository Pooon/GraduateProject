from GraduateProject import app
from flask import jsonify, request

@app.route('/user',methods = ['GET'])
def user_login():

	return 'Hello World!'
