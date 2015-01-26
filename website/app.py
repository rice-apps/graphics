from flask import Flask, request, redirect
import sqlite3 as sql
import smtplib

app = Flask(__name__)
# Database Connection
con = sql.connect('data.db')
cur = con.cursor()

@app.route("/")

# Bug Submission
@app.route("/bugs")
def bugs():
	name = request.form['name']
	email = request.form['email']
	return redirect('/')

# Idea Submission
@app.route("/ideas")
def ideas():
	return redirect('/')

# Application
@app.route("/apply")
def apply():
	name = request.form['inputName']
	email = request.form['riceID']
	phone = request.form['inputPhone']
	grade = request.form['year']
	major = request.form['inputMajor']
	#position
	#project
	interest = request.form['interest']
	#experience
	other_skills = request.form['other skills']
	comments = request.form['comments']




	return redirect('/')

