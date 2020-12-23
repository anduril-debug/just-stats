from bs4 import BeautifulSoup 
import requests


link = "/en/matches/26452511/Brighton-and-Hove-Albion-West-Bromwich-Albion-October-26-2020-Premier-League"





def get_match_possessions(link):
	r = requests.get("https://fbref.com"+link)


	all_teams = ["Arsenal","Aston Villa","Brighton & Hove Albion","Burnley","Chelsea","Crystal Palace","Everton","Fulham","Leeds United","Leicester City","Liverpool","Manchester City","Manchester United","Newcastle United","Sheffield United","Southampton","Tottenham Hotspur","West Bromwich Albion","West Ham United","Wolverhampton Wanderers"]


	soup = BeautifulSoup(r.content, 'html.parser')




	scores = soup.find_all(id="team_stats")

	trs = scores[0].find_all('tr')

	strongs = []

	for tr in trs:
		strong = tr.find_all('strong')
		if strong != []:
			strongs.append(strong)

	# teams = soup.find_all(attrs = {"itemprop" : "name" })


	# date = soup.find(class_="venuetime")


	tmp_dict = {
		"team1_possession" : strongs[0][0].text,
		"team2_possession" : strongs[0][1].text,
	}



	return tmp_dict






