from just_stats.models import Match,Team,Player,Match_Player_Stats,Used_Link,Upcoming_Match
from just_stats import db
from web_scrap.all_games import get_match, get_all_match_links
from web_scrap.match_detail import get_match_possessions
from web_scrap.players_stats import get_players_stats
from web_scrap.upcomings import get_all_matches,next_five_days
import uuid 

def link_is_used(link):

	links = Used_Link.query.all()

	for l in links:
		if l.used_link == link:
			return True
	return False

def update_teams(team1, team2, team1_score, team2_score):

	t1 = Team.query.filter_by(id = team1).first()
	t2 = Team.query.filter_by(id = team2).first()

	t1.goals_scored += team1_score
	t2.goals_scored += team2_score

	t1.goals_concended += team2_score
	t2.goals_concended += team1_score

	if team1_score > team2_score:
		t1.points += 3
		t1.wins += 1
		t2.loses += 1

		print(t1.name + " won the game")

	elif team1_score == team2_score:
		t1.points += 1
		t2.points += 1
		t1.draws += 1
		t2.draws += 1

		print("it's a draw")

	else:
		t2.points += 3
		t2.wins += 1
		t1.loses += 1

		print(t2.name + " won the game")

	db.session.commit()

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
		for k,v in p.items():
			if v == '' or v == ' ' or v == False or v == None:
				p[k] = '0'	

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
							shirt_number = p['shirt_number'], total_matches = 1,
							total_goals = p['goals'], total_assists = p['assists'], team_id = find_team_id(team_name))

			try:
				db.session.add(player)
				db.session.commit()
			except Exception as e:

				db.session.add(player)
				db.session.commit()
				raise e
			
			print('added new player ' + player.name)

def set_players_match_stats(players, match_id):
	
	for player in players:
		
		p = Player.query.filter_by(name = player['name']).first()

		for k,v in player.items():
			if v == '' or v == ' ' or v == False or v == None:
				player[k] = 0		

		stats = Match_Player_Stats( match_id = int(match_id), player_id = int(p.id), goals = int(player['goals']),
					assists = int(player['assists']), red_cards = int(player["cards_red"]), yellow_cards = int(player['cards_yellow']),
					minutes_played = int(player['minutes_played']), pens_made = int(player['penalties_made']), pens_att = int(player['penalties_att']), total_shots = int(player['total_shots']), shots_on_target = int(player['shots_on_target']),
					touches = int(player['touches']), pressures = int(player['pressures']), tackles = int(player['tackles']), interceptions = int(player['interceptions']), blocks = int(player['blocks']),
					passes = int(player['passes']), passes_completed = int(player['passes_completed']), passes_pct = float(player['passes_pct']), passes_progressive_distance = int(player['passes_progressive_distance']),
					carries = int(player['carries']), carry_progressive_distance = int(player['carry_progressive_distance']), dribbles = int(player['dribbles']), dribbles_completed = int(player['dribbles_completed']))
		print("added current match stats for " + player['name'])

		try:
			db.session.add(stats)
			db.session.commit()
		except Exception as e:

			db.session.add(stats)
			db.session.commit()	

			raise e



def main(link):
	
	all_matches_links = get_all_match_links(link)[1:]

	for match in all_matches_links:
		
		if link_is_used(match):
			print(match + ' IS USED!')
			continue

		print(match)
		m = get_match(match)

		first_team_id = Team.query.filter_by(name=m['team1']).first().id
		second_team_id = Team.query.filter_by(name=m['team2']).first().id
		
		current_match = Match( first_team_score = int(m['team1_score']),
								first_team_id = first_team_id, second_team_id = second_team_id,
								 second_team_score = int(m['team2_score']),
								team1_pos = get_match_possessions(match)['team1_possession'],
								team2_pos = get_match_possessions(match)['team2_possession'],
								date = m['date'])
		

		try:
			db.session.add(current_match)
			db.session.commit()
		except Exception as e:

			db.sessin.delete(current_match)
			db.session.commit()

			raise e
		
		print(current_match)
		print(current_match.date)

		update_teams(current_match.first_team_id, current_match.second_team_id,
					 current_match.first_team_score, current_match.second_team_score)

		players = get_players_stats(match)


		update_players(players['team1'], m['team1'])
		print("team1 updated")
		update_players(players['team2'], m['team2'])
		print("team2 updated")
		set_players_match_stats(players['team1'], match_id = current_match.id)
		set_players_match_stats(players['team2'], match_id = current_match.id)

		used_link = Used_Link(used_link = match)
		try:
			db.session.add(used_link)
			db.session.commit()
		except Exception as e:
			db.session.delete(current_match)
			db.session.commit()

			raise e

def upcoming_games():
	upcomings = next_five_days("https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures")

	upcoming_games = Upcoming_Match.query.delete()

	for match in upcomings:
		current_match = Upcoming_Match(
			uuid = uuid.uuid4(),
			team1 = match['team1'],
			team2 = match['team2'],
			date = match['date_time'])

		try:
			db.session.add(current_match)
			db.session.commit()
		except Exception as e:

			db.sessin.delete(current_match)
			db.session.commit()

			raise e

	return upcomings