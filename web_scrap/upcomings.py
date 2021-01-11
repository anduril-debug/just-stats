from bs4 import BeautifulSoup 
import requests
import datetime


def get_all_matches(link):

	r = requests.get(link)
	soup = BeautifulSoup(r.content, 'html.parser')
	trs = soup.find_all("tr", attrs={"class" : None})	
	matches = trs[1:]

	all_matches = []


	for match in matches:
		current_match = {
			"team1": None,
			"team2": None,
			"gameweek": None,
			"score": None,
			"date_time": None,
			"date": None,
			"time": None
		}

		current_match['team1'] = match.find(attrs={'data-stat' : 'squad_a'}).text
		current_match['team2'] = match.find(attrs={'data-stat' : 'squad_b'}).text
		current_match['gameweek'] = match.find(attrs={'data-stat' : 'gameweek'}).text
		current_match['score'] = match.find(attrs={'data-stat' : 'score'}).text


		if match.find(attrs={'data-stat': 'time'}).text == '' or match.find(attrs={'data-stat': 'date'}).text == '':
			current_match['date_time'] = 'Match Postponed'
		else:
			date_time = match.find(attrs={'data-stat': 'date'}).text + "_" + match.find(attrs={'data-stat': 'time'}).text
			date_time = ''.join(date_time.split())
			current_match['date_time'] = datetime.datetime.strptime(date_time,"%Y-%m-%d_%H:%M")

		if current_match['date_time'] == 'Match Postponed':
			continue
		else:
			current_match['date'] =	current_match['date_time'].date()
			current_match['time'] = current_match['date_time'].time()



		all_matches.append(current_match)

	return all_matches


#"https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"

# test = get_all_matches("https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures")


# for match in all_matches:
# 	print(match['date'], match['time'])



def next_five_days(link):

	all_matches = get_all_matches(link)
	next_five_days_games = []

	now = datetime.datetime.now()
	five_days = now + datetime.timedelta(days = 5)

	for match in all_matches:
		if match['date_time'] > now and match['date_time'] < five_days:
			next_five_days_games.append(match)


	return next_five_days_games



