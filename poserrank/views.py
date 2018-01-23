from flask import render_template, request
from poserrank import app
from poserrank import database as db

@app.route('/')
def index():
	return render_template('index.html.j2')

@app.route('/top/')
def top():
	posers = db.get_posers() # connect to the database and retrieve all posers
	return render_template('top.html.j2', posers=posers) # render the 'top' template, with posers as a local variable passed into the template

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html.j2')

    if request.method == 'POST':
        return "placeholder"
