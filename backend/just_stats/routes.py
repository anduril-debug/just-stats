from flask import render_template,url_for,request,jsonify
from flask_restful import Resource, marshal_with
from just_stats import app, api
from just_stats.models import Team,Player,Match_Player_Stats,Match,Upcoming_Match
from just_stats.fields import upcomings_fields,teams_fields,matches_fields,players_fields

from sqlalchemy import or_

import datetime
from json import JSONEncoder

# @app.route('/')
# def index():
# 	upcomings = Upcoming_Match.query.all()
# 	alt_names = {
# 		"Brighton": "Brighton & Hove Albion",
# 		"Sheffield Utd": "Sheffield United",
# 		"Newcastle Utd": "Newcastle United",
# 		"Tottenham": "Tottenham Hotspur",
# 		"West Ham" : "West Ham United",
# 		"Wolves" : "Wolverhampton Wanderers",
# 		"Manchester Utd": "Manchester United",
# 		"West Brom" : "West Bromwich Albion"
# 	}


# 	short_names = {
# 		"Burnley" : "BUR", "Everton" : "EVE", "West Ham" : "WHU", "Aston Villa" : "AVA",
# 		 "Manchester Utd" : "MUN", "Leeds United" : "LEE", "Tottenham" : "TOT", "Crystal Palace" : "CRY",
# 		 "Sheffield Utd" : "SHU", "Brighton" : "BRH", "Wolves" : "WLV", "Arsenal" : "ARS",
# 		 "West Brom" : "WBU", "Leicester City" : "LEI",
# 		 "Newcastle Utd" : "NEW", "Chelsea" : "CHE",
# 		  "Manchester City" : "MCI", "Liverpool" : "LIV", "Southampton" : "SOU", "Fulham" : "FUL"
# 	}


# 	return render_template('index.html', matches = matches, upcomings = upcomings, 
# 							alt_names = alt_names, short_names = short_names, datetime = datetime)



# @app.route('/teams')
# def teams():
# 	teams = Team.query.order_by(Team.points.desc(), (Team.goals_scored - Team.goals_concended).desc()).all()
# 	return render_template('teams.html', teams = teams)



# @app.route('/top_scorers')
# def top_scorers():
# 	top_scorers = Player.query.order_by(Player.total_goals.desc(), Player.total_assists.desc()).all()
# 	return render_template('top_scorers.html', top_scorers = top_scorers, teams = Team)


# @app.route('/matches')
# def matches():
# 	matches = Match.query.all()
# 	return render_template('matches.html', matches = matches)



# @app.route('/match/detail/<int:match_id>')
# def match_detail(match_id):
# 	match = Match.query.filter_by(id = match_id).first()
# 	return render_template('match_detail.html', match = match)


# @app.route('/players')
# def players():
# 	players = Player.query.order_by(Player.name).all()
# 	return render_template('players.html', players = players)


# @app.route('/player_detail/<int:player_id>')
# def player_detail(player_id):
# 	player = Player.query.filter_by(id = player_id).first()
# 	return render_template('player_detail.html', player = player, matches = Match)


# @app.route('/match_stats/<int:player_id>/<int:match_id>')
# def match_stats(player_id, match_id):
# 	match_stats = Match_Player_Stats.query.filter_by(player_id = player_id, match_id = match_id).first()
# 	match = Match.query.filter_by(id = match_id).first()
# 	player = Player.query.filter_by(id = player_id).first()
# 	return render_template('match_stats.html', match_stats = match_stats, match = match, player = player)



class Upcomings(Resource):
	@marshal_with(upcomings_fields)
	def get(self):
		upcomings = Upcoming_Match.query.all()
		return upcomings,201


class All_Teams(Resource):
	@marshal_with(teams_fields)
	def get(self):
		teams = Team.query.order_by(Team.points.desc(), (Team.goals_scored - Team.goals_concended).desc()).all()
		return teams,201


class All_Matches(Resource):
	@marshal_with(matches_fields)
	def get(self):
		matchs = Match.query.all()
		return matchs,201


class All_Last_Five(Resource):
	def get(self):
		teams = Team.query.order_by(Team.id).all()
		last_games = []
	

		for team in teams:
			team_name = team.name
			form = []
			last_five = team.last_five()

			for game in last_five[::-1]:
				if game.team_won() == team:
					form.append({
						"result": "W",
						"id": game.id
						})
				elif game.team_won() == "Draw":
					form.append({
						"result": "D",
						"id": game.id
					})
				else:
					form.append({
						"result": "L",
						"id": game.id
					})


			last_games.append({ 
				"name" : team_name,
				"form" : form
			})



		return last_games, 201


class Last_Five(Resource):
	@marshal_with(matches_fields)
	def get(self, team_name):
		last_five = Team.query.filter_by(name = team_name).first().last_five()

		return last_five, 201
			

class All_Players(Resource):
	@marshal_with(players_fields)
	def get(self):
		players = Player.query.all()
		return players,201


class Player_Details(Resource):
	@marshal_with(players_fields)
	def get(self,player_id):
		player = Player.query.filter_by(id = player_id).first()
		return player,201
	


api.add_resource(Upcomings, '/api/upcomings')
api.add_resource(All_Teams, '/api/teams')
api.add_resource(All_Matches, '/api/matches')
api.add_resource(All_Players, '/api/players')
api.add_resource(Player_Details,'/api/player/<int:player_id>')
api.add_resource(Last_Five, '/api/last_five/<team_name>')
api.add_resource(All_Last_Five, '/api/all_last_five')