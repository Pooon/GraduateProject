from flask import render_template
from GraduateProject import app
from GraduateProject.model.course import Course
from flask import request, jsonify

@app.route('/home')
def getHompage():
	
	return render_template('home.html')


@app.route('/allCourse',methods=['GET'])
def allCourse():

	return render_template('allCourses.html')

@app.route('/createCourse',methods=['GET'])
def createCourse():
    
    return render_template('createCourse.html')

@app.route('/myCourses',methods=['GET'])
def myCourses():

	return render_template('myCourses.html')