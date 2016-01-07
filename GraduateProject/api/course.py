from flask import render_template
from GraduateProject import app

from flask import request, jsonify
from . import ERROR_COURSE

from GraduateProject.model.course import Course
from GraduateProject.model.lecture import Lecture
from GraduateProject.model.user import User

class Error(object):
    ID_ERROR = {'err': ERROR_COURSE + 1,
                'msg': 'ID param is illegal'}
    NOT_FOUND = {'err': ERROR_COURSE + 2,
                 'msg': 'Course is not found'}
    NOT_PERMITTED = {'err': ERROR_COURSE + 3,
                     'msg': 'Course is not permitted'}


@app.route('/courseInfo',methods=['GET'])
def getCourseDetail():

    course_id = request.args.get('courseId','',type=str)
    course = Course.query.get(int(course_id))

    if course is not None:
        lectures = Lecture.query.filter_by(course_id = course_id).order_by(Lecture.lecture_id)
        user = User.query.get(int(course.tutor_id))

        if lectures is not None and user is not None:
            return render_template('courseInfo.html',course = course,lecture = lectures,user = user)

    return jsonify(stat=0,**Error.ID_ERROR), 400

@app.route('/lecturePlaying',methods=['GET'])
def lecturePlaying():

    course_id = request.args.get('courseId','',type=str)
    course = Course.query.get(int(course_id))

    lectures = Lecture.query.filter_by(course_id = course_id).order_by(Lecture.lecture_id)

    if course is not None and lectures is not None:
        return render_template('lecturePlaying.html',course = course,lecture = lectures)

    return jsonify(stat=0,**Error.ID_ERROR), 400
    
@app.route('/testCourseDetail',methods=['GET'])
def testGetCourseDetail():

    course_id = request.args.get('courseId','',type=str)
    course = Course.query.get(int(course_id))

    lectures = Lecture.query.filter_by(course_id = course_id).order_by(Lecture.lecture_id)

    if course is not None and lectures is not None:
        return jsonify(stat = 1,course = course.to_json,lecture = [i.to_json for i in lectures.all()]),200

    return jsonify(stat=0,**Error.ID_ERROR), 400
