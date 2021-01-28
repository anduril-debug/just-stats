from just_stats import db




class Match(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_team = db.Column(db.String(120), nullable=False)
	first_team_score = db.Column(db.Integer, nullable=False)
	second_team = db.Column(db.String(120), nullable=False)
	second_team_score = db.Column(db.Integer, nullable=False)
	team1_pos = db.Column(db.String(5))
	team2_pos = db.Column(db.String(5))
	date = db.Column(db.String(120), nullable=False)
	players_stats = db.relationship("Match_Player_Stats", backref='match', lazy=True)

	def __repr__(self):
		return f"{self.first_team} {self.first_team_score} - {self.second_team_score} {self.second_team}"



class Team(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), nullable=False)
	points = db.Column(db.Integer, nullable=False)
	wins = db.Column(db.Integer, nullable=False)
	draws = db.Column(db.Integer, nullable=False)
	loses = db.Column(db.Integer, nullable=False)
	goals_scored = db.Column(db.Integer, nullable=False)
	goals_concended = db.Column(db.Integer, nullable=False)
	players = db.relationship("Player", backref="team", lazy=True)

	def __repr__(self):
		return f"{self.name}"


class Player(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), nullable=False)
	
	age = db.Column(db.Integer, nullable=False)
	nationality = db.Column(db.String(120), nullable=False)
	shirt_number = db.Column(db.String(5))
	total_matches = db.Column(db.Integer)
	total_goals = db.Column(db.Integer)
	total_assists = db.Column(db.Integer)
	team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
	games_stats = db.relationship('Match_Player_Stats', backref='player', lazy=True)

	def __repr__(self):
		return f"{self.name}"






class Match_Player_Stats(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
	player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
	goals = db.Column(db.Integer, nullable=False)
	assists = db.Column(db.Integer, nullable=False)
	red_cards = db.Column(db.Integer, nullable=False)
	yellow_cards = db.Column(db.Integer, nullable=False)
	minutes_played = db.Column(db.Integer, nullable=False)
	pens_made = db.Column(db.Integer, nullable=False)
	pens_att = db.Column(db.Integer, nullable=False)
	total_shots = db.Column(db.Integer, nullable=False)
	shots_on_target = db.Column(db.Integer, nullable=False)
	touches = db.Column(db.Integer, nullable=False)
	pressures = db.Column(db.Integer, nullable=False)
	tackles = db.Column(db.Integer, nullable=False)
	interceptions = db.Column(db.Integer, nullable=False)
	blocks = db.Column(db.Integer, nullable=False)
	passes = db.Column(db.Integer, nullable=False)
	passes_completed = db.Column(db.Integer, nullable=False)
	passes_pct = db.Column(db.Integer, nullable=False)
	passes_progressive_distance = db.Column(db.Integer, nullable=False)
	carries = db.Column(db.Integer, nullable=False)
	carry_progressive_distance = db.Column(db.Integer, nullable=False)
	dribbles = db.Column(db.Integer, nullable=False)
	dribbles_completed = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"game ID {self.match_id} stats of player ID {self.player_id}"





class Used_Link(db.Model):
	used_link = db.Column(db.String(1024), nullable=False, primary_key=True)
	def __repr__(self):
		return self.used_link


class Upcoming_Match(db.Model):
	uuid = db.Column(db.String(512), primary_key=True)
	team1 = db.Column(db.String(120), nullable=False)
	team2 = db.Column(db.String(120), nullable=False)
	date = db.Column(db.String(50), nullable=False)

	def __repr__(self):
		return self.team1 + " vs " + self.team2






