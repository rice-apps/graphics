# app.py

# imports galore
from flask import Flask, request, redirect, g
import sqlite3 as sql
import smtplib
import config
from flask.ext.mail import Mail, Message
from datetime import datetime

app = Flask(__name__)
app.config.from_object(__name__)
# Email
mail = Mail(app)

# Database
@app.before_request
def before_request():
	g.db = sql.connect('apply.db', detect_types=sql.PARSE_DECLTYPES) #check_same_thread=False

@app.teardown_request
def teardown_request(exception):
	if hasattr(g, 'db'):
		g.db.close()

@app.route("/")
def index():
	return app.send_static_file("index.html")
@app.route("/teams")
def projects():
	return app.send_static_file("teams.html")
@app.route("/faq")
def faq():
	return app.send_static_file("faq.html")

@app.route("/images/<string:file_name>")
def images(file_name):
	return app.send_static_file("images/%s" % file_name)
@app.route("/css/<string:file_name>")
def css(file_name):
	return app.send_static_file("css/%s" % file_name)
@app.route("/js/<string:file_name>")
def js(file_name):
	return app.send_static_file("js/%s" % file_name)
@app.route("/fonts/<string:file_name>")
def fonts(file_name):
	return app.send_static_file("fonts/%s" % file_name)

@app.route("/contact", methods=["GET", "POST"])
def contact():
	if request.method == "GET":
		return app.send_static_file("contact.html")
	elif request.method == "POST":
		name = request.form['name']
		email = request.form['email']
		text = request.form['text']
		subject = ('Bug' if request.form['type'] == 'bug' else 'Idea') + ' Submission by %s' % name 
		print subject + "SHPGHPOIHEFPOQIHEG"
		msg = Message(text, sender=email, recipients=['xal1@rice.edu'], subject=subject)
		mail.send(msg)
		return redirect('/contact')

# # Idea Submission
# @app.route("/ideas", methods=["POST"])
# def ideas():
# 	name = request.form['name']
# 	email = request.form['email']
# 	idea_msg = request.form['idea']
# 	subject = 'Idea Submission by %s' % name 
# 	msg = Message(idea_msg, sender=email, recipients=['xal1@rice.edu'], subject=subject)
# 	mail.send(msg)
# 	return redirect('/')

# Application
@app.route('/apply', methods=["GET", 'POST'])
def apply():
	if request.method == "GET":
		return app.send_static_file("apply.html")
	elif request.method == "POST":
		name = request.form['name'] # applicant's name
		email = request.form['email'] # applicant's rice email
		grade = request.form['year'] # applicant's grade
		position = request.form.getlist('position') # position applying for
		project = request.form.getlist('project') # projects not desired
		skills = request.form['skills'] # applicant's skills
		comments = request.form['comments'] # additional comments
		task = request.form.getlist['mini_task'] # completed mini-task
		with con:
			g.db.execute("""INSERT INTO apply (name, email, phone, grade, major, position, project, skills, comments, task, timestamp) 
							VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
							(name, email, grade, major, position, project, skills, comments, task, datetime.now()))
			g.db.commit()
		return redirect('/apply')

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80, debug=True)

