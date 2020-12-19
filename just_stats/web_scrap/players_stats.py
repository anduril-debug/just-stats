from bs4 import BeautifulSoup 
import requests

link = "https://fbref.com/en/matches/cc230451/Liverpool-Leicester-City-November-22-2020-Premier-League"


def get_players_stats(link):
	r = requests.get("https://fbref.com"+link)

	soup = BeautifulSoup(r.content, 'html.parser')


	tables = soup.find_all('table', class_="stats_table")
	real_tables = [tables[0], tables[7]]


	team1 = []
	team2 = []


	for i in range(2):
		if i == 0:
			rows = real_tables[i].find_all('tr')
			team1 = rows[2:-1]
		elif i == 1:
			rows = real_tables[i].find_all('tr')
			team2 = rows[2:-1]




	team1_players = []
	team2_players = []


	for player in team1:
		tmp_d = {}
		tmp_d["name"] = player.a.text
		tmp_d["nationality"] = player.span.text
		tmp_d["position"] = player.find(attrs = {"data-stat" : "position" }).text
		tmp_d["shirt_number"] = player.find(attrs = {"data-stat" : "shirtnumber" }).text 
		tmp_d["age"] = player.find(attrs = {"data-stat" : "age" }).text
		tmp_d["minutes_played"] = player.find(attrs = {"data-stat" : "minutes" }).text
		tmp_d["goals"] = player.find(attrs = {"data-stat" : "goals" }).text 
		tmp_d["assists"] = player.find(attrs = {"data-stat" : "assists" }).text
		tmp_d["penalties_made"] = player.find(attrs = {"data-stat" : "pens_made" }).text
		tmp_d["penalties_att"] = player.find(attrs = {"data-stat" : "pens_att" }).text	
		tmp_d["total_shots"] = player.find(attrs = {"data-stat" : "shots_total" }).text
		tmp_d["shots_on_target"] = player.find(attrs = {"data-stat" : "shots_on_target" }).text
		tmp_d["cards_yellow"] = player.find(attrs = {"data-stat" : "cards_yellow" }).text
		tmp_d["cards_red"] = player.find(attrs = {"data-stat" : "cards_red" }).text
		tmp_d["touches"] = player.find(attrs = {"data-stat" : "touches" }).text
		tmp_d["pressures"] = player.find(attrs = {"data-stat" : "pressures" }).text
		tmp_d["tackles"] = player.find(attrs = {"data-stat" : "tackles" }).text
		tmp_d["interceptions"] = player.find(attrs = {"data-stat" : "interceptions" }).text
		tmp_d["blocks"] = player.find(attrs = {"data-stat" : "blocks" }).text	
		tmp_d["passes_completed"] = player.find(attrs = {"data-stat" : "passes_completed" }).text
		tmp_d["passes"] = player.find(attrs = {"data-stat" : "passes" }).text	
		tmp_d["passes_pct"] = player.find(attrs = {"data-stat" : "passes_pct" }).text	
		tmp_d["passes_progressive_distance"] = player.find(attrs = {"data-stat" : "passes_progressive_distance" }).text
		tmp_d["carries"] = player.find(attrs = {"data-stat" : "carries" }).text
		tmp_d["carry_progressive_distance"] = player.find(attrs = {"data-stat" : "carry_progressive_distance" }).text
		tmp_d["dribbles_completed"] = player.find(attrs = {"data-stat" : "dribbles_completed" }).text
		tmp_d["dribbles"] = player.find(attrs = {"data-stat" : "dribbles" }).text

		team1_players.append(tmp_d)


	for player in team2:
			tmp_d = {}
			tmp_d["name"] = player.a.text
			tmp_d["nationality"] = player.span.text
			tmp_d["position"] = player.find(attrs = {"data-stat" : "position" }).text
			tmp_d["shirt_number"] = player.find(attrs = {"data-stat" : "shirtnumber" }).text 
			tmp_d["age"] = player.find(attrs = {"data-stat" : "age" }).text
			tmp_d["minutes_played"] = player.find(attrs = {"data-stat" : "minutes" }).text
			tmp_d["goals"] = player.find(attrs = {"data-stat" : "goals" }).text 
			tmp_d["assists"] = player.find(attrs = {"data-stat" : "assists" }).text
			tmp_d["penalties_made"] = player.find(attrs = {"data-stat" : "pens_made" }).text
			tmp_d["penalties_att"] = player.find(attrs = {"data-stat" : "pens_att" }).text	
			tmp_d["total_shots"] = player.find(attrs = {"data-stat" : "shots_total" }).text
			tmp_d["shots_on_target"] = player.find(attrs = {"data-stat" : "shots_on_target" }).text
			tmp_d["cards_yellow"] = player.find(attrs = {"data-stat" : "cards_yellow" }).text
			tmp_d["cards_red"] = player.find(attrs = {"data-stat" : "cards_red" }).text
			tmp_d["touches"] = player.find(attrs = {"data-stat" : "touches" }).text
			tmp_d["pressures"] = player.find(attrs = {"data-stat" : "pressures" }).text
			tmp_d["tackles"] = player.find(attrs = {"data-stat" : "tackles" }).text
			tmp_d["interceptions"] = player.find(attrs = {"data-stat" : "interceptions" }).text
			tmp_d["blocks"] = player.find(attrs = {"data-stat" : "blocks" }).text	
			tmp_d["passes_completed"] = player.find(attrs = {"data-stat" : "passes_completed" }).text
			tmp_d["passes"] = player.find(attrs = {"data-stat" : "passes" }).text	
			tmp_d["passes_pct"] = player.find(attrs = {"data-stat" : "passes_pct" }).text	
			tmp_d["passes_progressive_distance"] = player.find(attrs = {"data-stat" : "passes_progressive_distance" }).text
			tmp_d["carries"] = player.find(attrs = {"data-stat" : "carries" }).text
			tmp_d["carry_progressive_distance"] = player.find(attrs = {"data-stat" : "carry_progressive_distance" }).text
			tmp_d["dribbles_completed"] = player.find(attrs = {"data-stat" : "dribbles_completed" }).text
			tmp_d["dribbles"] = player.find(attrs = {"data-stat" : "dribbles" }).text

			team2_players.append(tmp_d)

	result = { 
			"team1" : team1_players, 
			"team2" : team2_players
			}

	return result




