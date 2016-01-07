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

@app.route('/createCourseStep1',methods=['GET'])
def createCourseStep1():
	
	return render_template('createCourseStep1.html')

@app.route('createCourseStep2',methods=['GET'])
def createCourseStep2():
	
	return render_template('createCourseStep2.html')

@app.route('createCourseStep3',methods=['GET'])
def createCourseStep3():
	
	return render_template('createCourseStep3.html')