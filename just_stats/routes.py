from flask import render_template,url_for
from just_stats import app
from just_stats.models import Team,Player,Match_Player_Stats,Match



@app.route('/')
def index():
	return render_template('base.html')



@app.route('/teams')
def teams():
	teams = Team.query.all()
	return render_template('teams.html', teams = teams)