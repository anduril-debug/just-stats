from flask import render_template,url_for
from just_stats import app
from just_stats.models import Team,Player,Match_Player_Stats,Match



@app.route('/')
def index():
	return render_template('base.html')



@app.route('/teams')
def teams():
	teams = Team.query.order_by(Team.points.desc(), (Team.goals_scored - Team.goals_concended).desc()).all()
	return render_template('teams.html', teams = teams)



@app.route('/players')
def players():
	players = Player.query.order_by(Player.total_goals.desc(), Player.total_assists.desc()).all()
	return render_template('players.html', players = players, teams = Team)


@app.route('/matches')
def matches():
	matches = Match.query.all()
	return render_template('matches.html', matches = matches)



@app.route('/match/detail/<int:match_id>')
def match_detail(match_id):
	match = Match.query.filter_by(id = match_id).first()
	return render_template('match_detail.html', match = match)