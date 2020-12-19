from all_games import get_match, get_all_match_links
from match_detail import get_match_possessions
from players_stats import get_players_stats


link = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"


all_matches_links = get_all_match_links(link)[1:]

for i in all_matches_links:
	print("MATCH!")
	print("")
	print(get_match(i))
	print("################MATCH STATS##################")
	print(get_match_possessions(i))
	print("#########PLAYERS STATS##########")
	print(get_players_stats(i))
	print("")
	print("")