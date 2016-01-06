# -*- coding: utf-8 -*-
from GraduateProject import app, db
import course

class Lecture(db.Model):
	__tablename__ = 'lecture'

	lecture_id = db.Column(db.Integer, primary_key=True)
	lecture_name = db.Column(db.String(64), index=True)
	lecture_abstract = db.Column(db.String(600))
	course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'))
	video_url = db.Column(db.String(600))

	def __repr__(self):
		return '<Lecture %r>' % (self.coursename)
