from flask import render_template,url_for,request,jsonify
from flask_restful import Resource, marshal_with
from just_stats import app, api
from just_stats.models import Team,Player,Match_Player_Stats,Match,Upcoming_Match
from just_stats.fields import upcomings_fields,teams_fields,matches_fields,players_fields

from sqlalchemy import or_

import datetime
from json import JSONEncoder



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
						"score": f'{game.first_team} {game.first_team_score} - {game.second_team_score} {game.second_team}',
						"id": game.id
						})
				elif game.team_won() == "Draw":
					form.append({
						"result": "D",
						"score": f'{game.first_team} {game.first_team_score} - {game.second_team_score} {game.second_team}',
						"id": game.id
					})
				else:
					form.append({
						"result": "L",
						"score": f'{game.first_team} {game.first_team_score} - {game.second_team_score} {game.second_team}',
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