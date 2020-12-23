from flask import render_template
from just_stats import app
from just_stats.models import Player,Match_Player_Stats,Match



@app.route('/')
def index():
	return "HELLO WORLD"


@app.route('/players')
def players_view():
	players = Players.query.all()
	return render_template('players.html', players = players)



@app.route('/matches')
def matches_view():
	matches = Match.query.all()
	return render_template('matches.html', matches = matches)