from get_stats import main

link = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"


try:
	main(link)
except:
	print("Something went wrong.....")