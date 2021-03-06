# -*- coding: utf-8 -*-
from GraduateProject import app, db, login_manager
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
	__tablename__ = 'user'
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password_hash = db.Column(db.String(256), index=True, unique=True)
	email = db.Column(db.String(64), index=True, unique=True)
	#avatar_url = db.Column(db.String(200))
	
	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User %r>' % (self.username)

	#override method get_id in UserMixin
	def get_id(self):
		return self.user_id

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

