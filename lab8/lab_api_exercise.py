# -----------------------------------
# Lab API Exercise 
# -----------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# Step A - Download External Data
# -----------------------------------

url = "https://www.football-data.co.uk/mmz4281/2021/E0.csv"
file_name = "epl_matches.csv"

print("\nDownloading EPL data...")

try:
    matches = pd.read_csv(url)
    matches.to_csv(file_name, index=False)
    print("Download complete.")
except Exception as e:
    print("Download failed:", e)
    exit()

# -----------------------------------
# Step B - Load DataFrame
# -----------------------------------

print("\nPreview of data:")
print(matches.head())

# -----------------------------------
# Step C - Filter Liverpool vs Man City
# -----------------------------------

liverpool_vs_city = matches[
    ((matches['HomeTeam'] == 'Liverpool') & (matches['AwayTeam'] == 'Man City')) |
    ((matches['HomeTeam'] == 'Man City') & (matches['AwayTeam'] == 'Liverpool'))
]

print("\nFiltered Matches:")
print(liverpool_vs_city)

# -----------------------------------
# Step D - Calculate Averages
# -----------------------------------

home_avg_goals = liverpool_vs_city['FTHG'].mean()
away_avg_goals = liverpool_vs_city['FTAG'].mean()

print("\nAverage Goals:")
print("Home Team Average Goals:", home_avg_goals)
print("Away Team Average Goals:", away_avg_goals)

# -----------------------------------
# Step E - Visualization
# -----------------------------------

metrics = ['Home Goals', 'Away Goals']
values = [home_avg_goals, away_avg_goals]

plt.figure(figsize=(6, 4))
plt.bar(metrics, values)
plt.title("Liverpool vs Man City — Average Goals")
plt.ylabel("Average Goals")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

input("Press Enter to close...")