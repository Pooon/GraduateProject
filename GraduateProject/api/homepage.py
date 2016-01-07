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

@app.route('/myCourses',methods=['GET'])
def myCourses():

	return render_template('myCourses.html')

@app.route('/createCourse',methods=['GET'])
def createCourse():
    
    return render_template('createCourse.html')

@app.route('/createCourseStepFirst',methods=['GET'])
def createCourseStepFirst():
	
	return render_template('createCourseStepFirst.html')

@app.route('/createCourseStepSecond',methods=['GET'])
def createCourseStepSecond():
	
	return render_template('createCourseStepSecond.html')

@app.route('/createCourseStepThird',methods=['GET'])
def createCourseStepThird():
	
	return render_template('createCourseStepThird.html')