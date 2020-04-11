import requests

# primo tentativo

r = requests.get("https://api.chess.com/pub/club/team-toscana/matches")
toscana_matches = r.json()
toscana_finished = toscana_matches['finished']
print(toscana_finished)