"""
Ian Martinez
Lab 8: API'S
FEB 24, 2026
"""
# ---------------------------------
# Example 1: dataframe using pandas
# ---------------------------------
import pandas as pd
# dict_ as the static template of our API
dict_ = {
    'a' : [ 11,21,31],
    'b' : [12,22,32],
}
# create a dataframe using pandas
df = pd.DataFrame(dict_)


# head method of the dataframe communicates with the API displaying the first few rows of the dataframe
print("\n Example 1: simple API")
print(df.head())

# mean method calculates and returns the mean value of each row of the dataframe
print(f"The mean value is = {df.mean()}")

# ---------------------------------
# Example 2: Get NBA team from static.py file
# ---------------------------------
# step 1, data collection
from Static import get_teams   

nba_teams = get_teams()  # Get the list of NBA teams from the static.py file

#testing
print(f"The first two teams: {nba_teams[:2]}")
# step 2, create dataframe
df_teams = pd.DataFrame(nba_teams)  
print("\nAll teams")
print(df_teams.head()) 

# step 3 working with the data in df_teams
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']  
print('\nWarriors')
print(df_warriors)

# ---------------------------------
# Example 3: working with external APIs
# ---------------------------------
# step 1, data collection
#download the pickle file
import requests

url ="https://s3-api.us-geo.objectstorage.softlayer.net/cfcoursesdata/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

file_name = "Golden_State.pkl"

print("\nDownloading external file!....")

response = requests.get(url)

if response.status_code == 200:
    with open(file_name, 'wb') as f:
        f.write(response.content)
    print(f"File downloaded successfully and saved as {file_name}")
else:
    print(f"Failed to download file. Status code: {response.status_code}")

    # step 2, create dataframe
    # b. load dataframe from a pickle file
    games = pd.read_pickle(file_name)
    print(f"\nGames from pickle file:")
    print(games.head())

    # Step 3 - Working with the dataframe

# c. Filter GSW vs Raptors games
warriors_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]

# Separate home and away games
gsw_home_vs_raptors = warriors_vs_raptors[
    warriors_vs_raptors['MATCHUP'].str.contains('vs')
]

gsw_away_vs_raptors = warriors_vs_raptors[
    warriors_vs_raptors['MATCHUP'].str.contains(' @ ')
]

# Testing
print("\nGSW Home Games vs Raptors:")
print(gsw_home_vs_raptors)

print("\nGSW Away Games vs Raptors:")
print(gsw_away_vs_raptors)

# d. Calculate averages

home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()

home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

print("\nAverage PLUS_MINUS (Home):", home_avg_plus)
print("Average PLUS_MINUS (Away):", away_avg_plus)

print("\nAverage Points (Home):", home_avg_pts)
print("Average Points (Away):", away_avg_pts)

print(f"GSW home average = {home_avg_plus}")
print(f"GSW away average = {away_avg_plus}")    

# e.visualization of data analysis
import matplotlib.pyplot as plt

metrics = ['PLUS_MINUS', 'PTS']
home_values = [home_avg_plus, home_avg_pts]
away_values = [away_avg_plus, away_avg_pts]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8,5))
plt.bar([i - bar_width/2 for i in x], home_values, width=bar_width, label='Home', color='skyblue')
plt.bar([i - bar_width/2 for i in x], away_values, width=bar_width, label='Away', color='orange')

plt.xticks(x, metrics)
plt.title("GSW vs Raptors")

plt.ylabel("Average Values")
plt.legend()
plt.show(block=True)

input("Press Enter to close...")