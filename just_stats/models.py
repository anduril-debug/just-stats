from just_stats import db




class Match(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_team = db.Column(db.String(120), nullable=False)
	first_team_score = db.Column(db.String(5), nullable=False)
	second_team = db.Column(db.String(120), nullable=False)
	second_team_score = db.Column(db.String(5), nullable=False)
	date = db.DateTime()
	players_stats = db.relationship("Match_Player_Stats", backref='match', lazy=True)

	def __repr__(self):
		return f"{self.first_team} {self.first_team_score} - {self.second_team_score} {self.second_team}"



class Team(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), nullable=False)
	points = db.Column(db.Integer)
	goals_scored = db.Column(db.Integer)
	goals_concended = db.Column(db.Integer)
	players = db.relationship("Player", backref="team", lazy=True)

	def __repr__(self):
		return f"{self.name}"


class Player(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), nullable=False)
	age = db.Column(db.Integer, nullable=False)
	nationality = db.Column(db.Integer, nullable=False)
	shirt_number = db.Column(db.String(5))
	total_matches = db.Column(db.Integer)
	total_goals = db.Column(db.Integer)
	total_assists = db.Column(db.Integer)
	team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

	def __repr__(self):
		return f"{self.name}"






class Match_Player_Stats(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
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
		return f"{self.match_id} stats of {self.player_id}"

















