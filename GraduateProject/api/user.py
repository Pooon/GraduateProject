from GraduateProject import app
from flask import jsonify, request, url_for, render_template, flash, redirect
from GraduateProject import app, db
from flask.ext.login import login_user, logout_user, login_required
from GraduateProject.forms.auth_forms import LoginForm, RegistrationForm
from GraduateProject.model.user import User

@app.route('/login',methods = ['GET', 'POST'])
def user_login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('homepage'))
		flash('Invalid username or password')
	print('not validate')
	return render_template('login.html', form = form)


@app.route('/logout')
@login_required
def log_out():
	logout_user()
	return redirect(url_for('/'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
					username=form.username.data,
					password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('You can now login')
		return redirect(url_for('user_login'))
	return render_template('register.html', form=form)

