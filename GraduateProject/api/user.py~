from GraduateProject import app
from flask import jsonify, request, url_for, render_template, flash, redirect, make_response, jsonify
import json
from GraduateProject import app, db
from flask.ext.login import login_user, logout_user, login_required
from GraduateProject.forms.auth_forms import LoginForm, RegistrationForm
from GraduateProject.model.user import User

@app.route('/login',methods = ['GET', 'POST'])
def user_login():
#	form = LoginForm()
#	if form.validate_on_submit():
#		user = User.query.filter_by(email=form.email.data).first()
#		if user is not None and user.verify_password(form.password.data):
#			login_user(user, form.remember_me.data)
#			return redirect(request.args.get('next') or url_for('homepage'))
#		flash('Invalid username or password')
#	print('not validate')
#	return render_template('login.html', form = form)
	if request.method == "GET":
		#show login form
		return '200'
	elif request.method == "POST":
		email = request.form.get('email')
		password = request.form.get('password')
		remember_me = bool(request.form.get('remember_me'))
		user = User.query.filter_by(email=email).first()
		if user is not None and user.verify_password(password):
			login_user(user, remember_me)
			return make_response(json.dumps({'username':user.username}), 200)
		return '403'		


@app.route('/logout')
@login_required
def log_out():
	logout_user()
	return redirect(url_for('/'))

@app.route('/register', methods=['GET', 'POST'])
def register():
#	form = RegistrationForm()
#	if form.validate_on_submit():
#		user = User(email=form.email.data,
#					username=form.username.data,
#					password=form.password.data)
#		db.session.add(user)
#		db.session.commit()
#		flash('You can now login')
#		return redirect(url_for('user_login'))
#	return render_template('register.html', form=form)
	if request.method == "GET":
		#show register form
		return '404'
	elif request.method == "POST":
		email = request.form.get('email')
		password = request.form.get('password')
		username = request.form.get('username')
		if email is None or password is None or username is None:
			return '403'
		user = User(email=email,
					username=username,
					password=password)
		db.session.add(user)
		db.session.commit()
		return '200'

