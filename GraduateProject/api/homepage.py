from flask import render_template
from GraduateProject import app
from GraduateProject.model.course import Course
from flask import request, jsonify

@app.route('/homePage')
def getHompage():
	
	return render_template('FirstPage.html')


@app.route('/allCourse',methods=['GET'])
def allCourse():

	return render_template('allCourses.html')
