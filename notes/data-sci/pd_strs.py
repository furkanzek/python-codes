import pandas as pd

data = pd.read_csv('C:/Users/furka/OneDrive/Masaüstü/python-codes/PyCharm/nba.csv')
data.dropna(inplace=True)

data['player_name'] = data['player_name'].str.upper()
data['player_name'] = data['player_name'].str.lower()
data['index'] = data['player_name'].str.find('f')
data = data[data.player_name.str.contains('james')]
data = data.team_abbreviation.str.replace('A', 'X').str.replace('S', 'W')
data[['first_name', 'last_name']] = data['player_name'].loc[data['player_name'].str.len()==2].str.split()

print(data.head(10))