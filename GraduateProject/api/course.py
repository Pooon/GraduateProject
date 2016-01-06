from flask import render_template
from GraduateProject import app
from GraduateProject.model.course import Course
from flask import request, jsonify

class Error(object):
    ID_ERROR = {'err': ERROR_COURSE + 1,
                'msg': 'ID param is illegal'}
    NOT_FOUND = {'err': ERROR_COURSE + 2,
                 'msg': 'Course is not found'}
    NOT_PERMITTED = {'err': ERROR_COURSE + 3,
                     'msg': 'Course is not permitted'}


@app.route('/courseDetail',methods=['GET'])
def getCourseDetail():

	course_id = request.args.get('courseId', '', type=str)
	course = Course.query.filter_by(course_id).first()

    if course is not None:
        return render_template('lecturePlaying.html'，course = course)

    return jsonify(stat=0, **Error.ID_ERROR), 400