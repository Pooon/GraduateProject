# -*- coding: utf-8 -*-
from GraduateProject import app, db
import course

class Lecture(db.Model):
	__tablename__ = 'lecture'

	lecture_id = db.Column(db.Integer, primary_key=True)
	lecture_name = db.Column(db.String(64), index=True)
	order = db.Column(db.Integer)
	lecture_abstract = db.Column(db.String(600))
	course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'))
	video_url = db.Column(db.String(600))

	def __repr__(self):
		return '<Lecture %r>' % (self.lecture_name)

	@property
	def to_json(self):
		return {
			'lecture_id': self.lecture_id,
			'lecture_name': self.lecture_name,
			'course_id': self.course_id,
			'order': self.order,
			'video_url': self.video_url,
			'lecture_abstract': self.lecture_abstract,
		}