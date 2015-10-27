from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'} #fake user
	posts = [ #fake array of posts
		{
			'author': {'nickname': 'John'},
			'body' : "I'm loving the weather today"
		},
		{
			'author': {'nickname': 'Carson'},
			'body': 'Security programming is the best'
		}
	]
	return render_template('index.html', title = 'Home', user = user, posts = posts)
