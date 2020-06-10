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
        partite = api.json()
        finite = partite["finished"]
        incorso = partite["in_progress"]
        registrate = partite["registered"]
        tutte = finite + incorso + registrate

        print("\n===== Elenco partite " + self.nome + " =====")
        # il ciclo cerca tutte le partite della squadra che hanno il nome specificato nella variabile torneo
        for p in tutte:
            titolo = p.get("name")
            risultato = p.get("result")
            if torneo in titolo or alternativa in titolo:
                if risultato == "win":
                    print("\033[32m" + titolo)
                if risultato == "lose":
                    print("\033[31m" + titolo)
                if risultato is None:
                    print("\033[37m" + titolo)


    def elenco_giocatori(self, api):
        giocatori = api.json()
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

basilicata = Regione("Basilicata")
basilicata.elenco_risultati(requests.get("https://api.chess.com/pub/club/team-basilicata/matches"))
