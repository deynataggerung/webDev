from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')

@app.route('/login')
def login():
	return "hello world"
	#form = LoginForm()
	#if form.validate_on_submit():
	#	flash('Login Requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
	#	return redirect('/index')
	#return render_template('login.html', title="Sign In", form=form)
