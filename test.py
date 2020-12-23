from just_stats.models import Match,Team,Player,Match_Player_Stats
from just_stats import db

from web_scrap.all_games import get_match, get_all_match_links
from web_scrap.match_detail import get_match_possessions
from web_scrap.players_stats import get_players_stats



def find_team_id(team_name):
	teams = Team.query.all()
	for t in teams:
		if t.name == team_name:
			return t.id

def player_exists(name):
	players = Player.query.all()

	for p in players:
		if p.name == name:
			return True
	return False

def update_players(team, team_name):
	for p in team:
		player = Player.query.filter_by(name = p['name']).first()

		if player:
			player.age = int(p['age'][:2])
			player.shirt_number = p['shirt_number']
			player.total_matches += 1
			player.total_goals += int(p['goals'])
			player.total_assists += int(p['assists'])
			player.team_id = find_team_id(team_name)

			db.session.commit()
			print('updated player ' + player.name)

		else:
			player = Player(name = p['name'], age = int(p['age'][:2]), nationality = p['nationality'],
							shirt_number = p['shirt_number'], total_matches = 0,
							total_goals = 0, total_assists = 0, team_id = find_team_id(team_name))
			db.session.add(player)
			db.session.commit()
			print('added new player ' + player.name)


link = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"


all_matches_links = get_all_match_links(link)[1:2]

for match in all_matches_links:
	m = get_match(match)

	current_match = Match(first_team = m['team1'], first_team_score = int(m['team1_score']),
					second_team = m['team2'], second_team_score = int(m['team2_score']),
						date = m['date'])
	print(current_match)
	print(current_match.date)

	players = get_players_stats(match)

	t1_players = players['team1']
	t2_players = players['team2']

	update_players(t1_players, m['team1'])
	update_players(t2_players, m['team2'])
