# -*- coding: utf-8 -*-
from GraduateProject import app, db
import lecture
import category

class Course(db.Model):
	__tablename__ = 'course'
	course_id = db.Column(db.Integer, primary_key=True)
	course_name = db.Column(db.String(64), index=True, unique=True)
	course_abstract = db.Column(db.String(600))
	tutor_id = db.Column(db.Integer, index=True)
	category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
	lectures = db.relationship('Lecture', backref='course')

	def __repr__(self):
		return '<Course %r>' % (self.course_name)

	@property
	def to_json(self):
		return {
			'course_id': self.course_id,
			'course_name': self.course_name,
			'tutor_id': self.tutor_id,
			'category_id': self.category_id,
		}
