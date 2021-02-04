from just_stats import db
from just_stats.models import Team

db.drop_all()
db.create_all()


all_teams = [
	{
		"name": "Arsenal",
		"short_name" : "ARS",
		"nick_name": "The Gunners"
	},
	{
		"name": "Aston Villa",
		"short_name" : "AVA",
		"nick_name": "The Villans"
	},
	{
		"name": "Brighton & Hove Albion",
		"short_name" : "BRH",
		"nick_name": "The Seagulls"
	},	
	{
		"name": "Burnley",
		"short_name" : "BUR",
		"nick_name": "The Clarets"
	},	
	{
		"name": "Chelsea",
		"short_name" : "CHE",
		"nick_name": "The Blues"
	},	
	{
		"name": "Crystal Palace",
		"short_name" : "CRY",
		"nick_name": "The Eagles"
	},	
	{
		"name": "Everton",
		"short_name" : "EVE",
		"nick_name": "The Toffees"
	},	
	{
		"name": "Fulham",
		"short_name" : "FUL",
		"nick_name": "Cottagers"
	},	
	{
		"name": "Leeds United",
		"short_name" : "LEE",
		"nick_name": "The Whites"
	},	
	{
		"name": "Leicester City",
		"short_name" : "LEI",
		"nick_name": "The Foxes"
	},	
	{
		"name": "Liverpool",
		"short_name" : "LIV",
		"nick_name": "The Reds"
	},	
	{
		"name": "Manchester City",
		"short_name" : "MCI",
		"nick_name": "The Citizens"
	},	
	{
		"name": "Manchester United",
		"short_name" : "MUN",
		"nick_name": "The Red Devils"
	},
	{
		"name": "Newcastle United",
		"short_name" : "NEW",
		"nick_name": "The Magpies"
	},
	{
		"name": "Sheffield United",
		"short_name" : "SHU",
		"nick_name": "The Blades"
	},
	{
		"name": "Southampton",
		"short_name" : "SOU",
		"nick_name": "The Saints"
	},
	{
		"name": "Tottenham Hotspur",
		"short_name" : "TOT",
		"nick_name": "The Yid Army"
	},
	{
		"name": "West Bromwich Albion",
		"short_name" : "WBA",
		"nick_name": "The Baggies"
	},
	{
		"name": "West Ham United",
		"short_name" : "WHU",
		"nick_name": "The Hammers"
	},
	{
		"name": "Wolverhampton Wanderers",
		"short_name" : "WLV",
		"nick_name": "Wolves"
	}


]

for team in all_teams:
	t = Team(name = team['name'], short_name = team['short_name'], nickname = team['nick_name'], points = 0, wins = 0, draws = 0, loses = 0, goals_scored = 0, goals_concended = 0)
	db.session.add(t)
	db.session.commit()