from bs4 import BeautifulSoup 
import requests



def get_all_match_links(link):

	r = requests.get(link)

	soup = BeautifulSoup(r.content, 'html.parser')
	scores = soup.find_all(attrs={"data-stat": "score"})

	all_matches_links = []

	for i in scores:
		if len(i) > 0:
			all_matches_links.append((str(i.a)[9:-9]))

	return all_matches_links


def get_match(link):
	r = requests.get("https://fbref.com/"+link)
	all_teams = ["Arsenal","Aston Villa","Brighton & Hove Albion","Burnley","Chelsea","Crystal Palace","Everton","Fulham","Leeds United","Leicester City","Liverpool","Manchester City","Manchester United","Newcastle United","Sheffield United","Southampton","Tottenham Hotspur","West Bromwich Albion","West Ham United","Wolverhampton Wanderers"]
	soup = BeautifulSoup(r.content, 'html.parser')

	scores = soup.find_all(class_="score")
	teams = soup.find_all(attrs = {"itemprop" : "name" })
	date = soup.find(class_="venuetime")

	tmp_dict = {
		"team1" : None,
		"team1_score" : None,
		"team2" : None,
		"team2_score" : None,
		"date" : None
	}

	#ADDING TO DICTIONARY TEAM1 AND TEAM2

	teams_list = []
	for i in teams:
		if str(i.text) in all_teams:
			teams_list.append(i.text)

	for i in range(2):
		if i == 0:
			tmp_dict["team1"] = teams_list[i]
		else:
			tmp_dict["team2"] = teams_list[i]



	#ADDING SCORES TO DICTIONARY TEAM1_SCORE AND TEAM2_SCORE
	teams_score = []
	for i in scores:
		teams_score.append(i.text)

	for i in range(2):
		if i == 0:
			tmp_dict["team1_score"] = teams_score[i]
		else:
			tmp_dict["team2_score"] = teams_score[i]



	#ADDING DATETIME TO DICTIONARY
	tmp_dict["date"] = f"{date['data-venue-date']} {date['data-venue-time']}"


	return tmp_dict





