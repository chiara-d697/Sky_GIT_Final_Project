from flask import render_template
from application import app


@app.route('/')
@app.route('/home', endpoint='home')
def home():
    return render_template('home.html', title="Home")

@app.route('/new-gods-nezha-reborn')
def newgodsnezhareborn():
    return render_template('new-gods-nezha-reborn.html', title="New Gods: Nezha Reborn")

