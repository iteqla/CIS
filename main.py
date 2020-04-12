import requests
torneo = "CIS2020"

def toscana_elenco_partite():
    all_matches = requests.get("https://api.chess.com/pub/club/team-toscana/matches")
    partite = all_matches.json()
    finite = partite["finished"]
    print("\n===== Elenco partite Toscana =====")
    for x in finite:
        titolo = x.get("name")
        risultato = x.get("result")
        if torneo in titolo:
            print(titolo, risultato)



def abruzzo_elenco_partite():
    r = requests.get("https://api.chess.com/pub/club/team-abruzzo/matches")
    partite = r.json()
    finite = partite["finished"]
    print("\n===== Elenco partite Abruzzo =====")
    for x in finite:
        titolo = x.get("name")
        risultato = x.get("result")
        if torneo in titolo:
            print(titolo, risultato)

toscana_elenco_partite()
abruzzo_elenco_partite()