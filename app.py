# app.py

# imports galore
from flask import Flask, request, redirect, g
import sqlite3 as sql
import smtplib
import config
from flask.ext.mail import Mail, Message

app = Flask(__name__)
app.config.from_object(__name__)
# Email
mail = Mail(app)

# Database
@app.before_request
def before_request():
	g.db = sql.connect('test.db') #check_same_thread=False

@app.teardown_request
def teardown_request(exception):
	if hasattr(g, 'db'):
		g.db.close()

@app.route("/")
def index():
	return app.send_static_file("index.html")

# Bug Submission
@app.route("/bugs")
def bugs():
	name = request.form['name']
	email = request.form['email']
	bug_msg = request.form['bug']
	subject = 'Bug Submission by %s' % name 
	#msg = Message(bug_msg, sender=email, recipients=['xal1@rice.edu'], subject=subject)
	mail.send(msg)
	return redirect('/')

# Idea Submission
@app.route("/ideas")
def ideas():
	name = request.form['name']
	email = request.form['email']
	idea_msg = request.form['idea']
	subject = 'Idea Submission by %s' % name 
	#msg = Message(idea_msg, sender=email, recipients=['xal1@rice.edu'], subject=subject)
	mail.send(msg)
	return redirect('/')

# Application
@app.route('/apply', methods = ['POST'])
def apply():
	name = request.form['name'] # applicant's name
	email = request.form['email'] # applicant's rice email
	grade = request.form['year'] # applicant's grade
	position = request.form.getlist('position') # position applying for
	project = request.form.getlist('project') # projects not desired
	skills = request.form['skills'] # applicant's skills
	comments = request.form['comments'] # additional comments
	task = request.form.getlist['mini_task'] # completed mini-task
	with con:
		g.db.execute("""INSERT INTO apply (name, email, phone, grade, major, position, project, skills, comments, task) 
						VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
						(name, email, grade, major, position, project, skills, comments, task))
		g.db.commit()
	return redirect('/')

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80)

