from just_stats.models import Match,Team,Player,Match_Player_Stats
from just_stats import db

from web_scrap.all_games import get_match, get_all_match_links
from web_scrap.match_detail import get_match_possessions
from web_scrap.players_stats import get_players_stats



link = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"


all_matches_links = get_all_match_links(link)[1:20]


