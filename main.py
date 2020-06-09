import requests
torneo = "CIS2020"
alternativa = "CSI2020"

class Regione:
    def __init__(self, nome):
        self.nome = nome
        self.giocatori = None
        self.partite = None
        self.punteggio = None

    def elenco_risultati(self, api):
        self.partite = api.json()
        self.finite = self.partite["finished"]
        print("\n===== Elenco partite " + self.nome + " =====")
        for p in self.finite:
            titolo = p.get("name")
            risultato = p.get("result")
            if torneo in titolo or alternativa in titolo:
                print(titolo, risultato)

    def elenco_giocatori(self, api):
        self.giocatori = api.json()
        self.tutti = self.giocatori["all_time"]
        print("\n===== Elenco giocatori " + self.nome + " =====")
        for g in self.tutti:
            username = g.get("username")
            print(username)


toscana = Regione("Toscana")
toscana.elenco_risultati(requests.get("https://api.chess.com/pub/club/team-toscana/matches"))
toscana.elenco_giocatori(requests.get("https://api.chess.com/pub/club/team-toscana/members"))

calabria = Regione("Calabria")
calabria.elenco_risultati(requests.get("https://api.chess.com/pub/club/team-calabria/matches"))


