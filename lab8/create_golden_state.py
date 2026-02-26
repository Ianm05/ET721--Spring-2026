import pandas as pd

# Create a realistic game-level dataset
data = {
    "GAME_DATE": [
        "2023-01-01",
        "2023-01-15",
        "2023-02-01",
        "2023-02-15",
        "2023-03-01",
        "2023-03-15"
    ],
    "MATCHUP": [
        "GSW vs TOR",
        "GSW @ TOR",
        "GSW vs TOR",
        "GSW @ TOR",
        "GSW vs LAL",
        "GSW @ BOS"
    ],
    "PTS": [120, 108, 115, 102, 130, 99],
    "PLUS_MINUS": [15, -5, 8, -12, 20, -3]
}

games = pd.DataFrame(data)

games.to_pickle("Golden_State.pkl")

print("Golden_State.pkl recreated with correct structure!")