# -*- coding: utf-8 -*-
from GraduateProject import app, db
import course

class Category(db.Model):
	__tablename__ = 'category'
	category_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(128), index=True, unique=True)
	courses = db.relationship('Course', backref='category')

	def __repr__(self):
		return '<Category %r>' % (self.title)
