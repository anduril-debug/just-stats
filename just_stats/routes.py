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



@app.route('/top_scorers')
def top_scorers():
	top_scorers = Player.query.order_by(Player.total_goals.desc(), Player.total_assists.desc()).all()
	return render_template('top_scorers.html', top_scorers = top_scorers, teams = Team)


@app.route('/matches')
def matches():
	matches = Match.query.all()
	return render_template('matches.html', matches = matches)



@app.route('/match/detail/<int:match_id>')
def match_detail(match_id):
	match = Match.query.filter_by(id = match_id).first()
	return render_template('match_detail.html', match = match)


@app.route('/players')
def players():
	players = Player.query.order_by(Player.name).all()
	return render_template('players.html', players = players)


@app.route('/player_detail/<int:player_id>')
def player_detail(player_id):
	player = Player.query.filter_by(id = player_id).first()
	return render_template('player_detail.html', player = player, matches = Match)


@app.route('/match_stats/<int:player_id>/<int:match_id>')
def match_stats(player_id, match_id):
	match_stats = Match_Player_Stats.query.filter_by(player_id = player_id, match_id = match_id).first()
	match = Match.query.filter_by(id = match_id).first()
	player = Player.query.filter_by(id = player_id).first()
	return render_template('match_stats.html', match_stats = match_stats, match = match, player = player)


@app.route('/test')
def test():
	return {"test" : "test textinho"}