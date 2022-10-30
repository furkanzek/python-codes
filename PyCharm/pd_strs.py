import pandas as pd

data = pd.read_csv('nba.csv')
data.dropna(inplace=True)

data['player_name'] = data['player_name'].str.upper()

print(data)