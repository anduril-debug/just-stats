from flask_restful import fields

upcomings_fields = {
	'uuid' : fields.String,
	'team1': fields.String,
	'team2' : fields.String,
	'date' : fields.String
}


teams_fields = {
	'id' : fields.Integer,
	'name' : fields.String,
	'points' : fields.Integer,
	'wins' : fields.Integer,
	'draws': fields.Integer,
	'loses' : fields.Integer,
	'goals_scored' : fields.Integer,
	'goals_concended' : fields.Integer,
}

matches_fields = {
	'id' : fields.Integer,
	'first_team' : fields.String,
	'first_team_score' : fields.Integer,
	'second_team' : fields.String,
	'second_team_score' : fields.Integer,
	'team1_pos' : fields.String,
	'team2_pos' : fields.String,
	'date' : fields.String
}

players_fields = {
	'id' : fields.Integer,
	'name' : fields.String,
	'age' : fields.Integer,
	'nationality' : fields.String,
	'shirt_number' : fields.String,
	'total_matches' : fields.Integer,
	'total_goals' : fields.Integer,
	'total_assists' : fields.Integer,
	'team': fields.String 
}