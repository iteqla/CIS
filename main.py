import requests
import json

torneo = "CIS2020"
alternativa = "CSI2020"


class Regione:
    def __init__(self, api):
        self.nome = requests.get(api).json().get("name")
        self.giocatori = api + "/members"
        self.partite = api + "/matches"
        self.punteggio = None

    def elenco_risultati(self):
        partite = requests.get(self.partite).json()
        finite = partite["finished"]
        incorso = partite["in_progress"]
        registrate = partite["registered"]
        tutte = finite + incorso + registrate

        print("\033[34m" + "\n===== Elenco partite " + self.nome + " =====")
        # il ciclo cerca tutte le partite della squadra che hanno il nome specificato nella variabile torneo
        for p in tutte:
            titolo = p.get("name")
            risultato = p.get("result")
            avversario = requests.get(p.get("opponent")).json()
            if torneo in titolo or alternativa in titolo:
                if risultato == "win":
                    print("\033[32m" + avversario.get("name"))
                if risultato == "lose":
                    print("\033[31m" + avversario.get("name"))
                if risultato is None:
                    print("\033[37m" + avversario.get("name"))

    def elenco_giocatori(self):
        giocatori = requests.get(self.giocatori).json()
        sempre = giocatori["all_time"]
        weekly = giocatori["weekly"]
        monthly = giocatori["monthly"]
        tutti = sempre + weekly + monthly
        print("\n===== Elenco giocatori " + self.nome + " =====")
        for g in tutti:
            username = g.get("username")
            print(username)


# toscana = Regione("Toscana")
# toscana.elenco_risultati(requests.get("https://api.chess.com/pub/club/team-toscana/matches"))
# toscana.elenco_giocatori(requests.get("https://api.chess.com/pub/club/team-toscana/members"))
#
# calabria = Regione("Calabria")
# calabria.elenco_risultati(requests.get("https://api.chess.com/pub/club/team-calabria/matches"))

basilicata = Regione("https://api.chess.com/pub/club/team-basilicata")
basilicata.elenco_risultati()
# basilicata.elenco_giocatori()

toscana = Regione("https://api.chess.com/pub/club/team-toscana")
toscana.elenco_risultati()
# toscana.elenco_giocatori()
