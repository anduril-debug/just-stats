from get_stats import main, upcoming_games

link = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"


try:
	main(link)
	upcoming_games()
except:
	print("Something went wrong.....")