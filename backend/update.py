from get_stats import main, upcoming_games
from just_stats.models import Match,Team,Player, Match_Player_Stats


link = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"






try:
	main(link)
	upcoming_games()
except Exception as e:
	raise e