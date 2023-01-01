import requests
from bs4 import BeautifulSoup
import pandas as pd

league_id = 38458828
season_id = 2022
espn_cookies = {
      'swid': '{4131C795-BB33-48C6-A63F-C6CB9B9E45A8}',
      'espn_s2': 'AECDmatkg96WGvmUR9PVliLRwEY788zrR9K1bsXdHn3wF4ZVIr9HQen6DoF6Y8yx5nWUW0sB0WIxWHmEzTlUfaSIgDjnTOdQbDowoUm9dlwrUxJx2OQ3AfrG4muTHtI43am%2Be8w4Uy4%2FbnAZQ3bncfPba9q18Lbi7y7L%2BUVJXquHXZUDmbRHPR5x3XYrp9WZPwgmvDtTpJOQaJYUJdziR9m%2FGy0VGlGmCooUUBOO%2BSEvp6mx%2BaiPQj1t9uD4s6uc5skPPhLIPaZkXyDxfHgJS%2BcUBLMAqb2X3H7e9spcf0483g%3D%3D'
      }
# url = "https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/" + \
#       str(league_id) + "?seasonId=" + str(year)

# r = requests.get('https://fantasy.espn.com/apis/v3/games/ffl/seasons/2022/segments/0/leagues/38458828?view=mDraftDetail&view=mSettings&view=mTeam&view=modular&view=mNav',
#                  cookies={
#                     'swid': '{4131C795-BB33-48C6-A63F-C6CB9B9E45A8}',
#                     'espn_s2': 'AECDmatkg96WGvmUR9PVliLRwEY788zrR9K1bsXdHn3wF4ZVIr9HQen6DoF6Y8yx5nWUW0sB0WIxWHmEzTlUfaSIgDjnTOdQbDowoUm9dlwrUxJx2OQ3AfrG4muTHtI43am%2Be8w4Uy4%2FbnAZQ3bncfPba9q18Lbi7y7L%2BUVJXquHXZUDmbRHPR5x3XYrp9WZPwgmvDtTpJOQaJYUJdziR9m%2FGy0VGlGmCooUUBOO%2BSEvp6mx%2BaiPQj1t9uD4s6uc5skPPhLIPaZkXyDxfHgJS%2BcUBLMAqb2X3H7e9spcf0483g%3D%3D'
#                     }
#                 )
# res = r.json()
# print(len(res))
# print(res.keys())
# for k, v in res.items():
#       print(f"{k}: {type(v)}")

# print(res["status"])



url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/{}?view=proTeamSchedules_wl".format(season_id)
r = requests.get(url, cookies=espn_cookies)
team_data = r.json()
team_names = team_data['settings']['proTeams']
df = pd.DataFrame(team_names)  # get only needed columns for teams
team_df = df[['id', 'location', 'name']]
team_df["team name"] = team_df['location'].astype(str) +" "+ team_df["name"]  # rename in column
team_df.rename(columns = {'id':'team_id'}, inplace = True)

# soup = BeautifulSoup(r.content, 'html.parser')
# table = soup.find('table', class_='playerTableTable')
# tdf = pd.read_html(str(table), flavor='bs4')[0]

print(team_df.head())
