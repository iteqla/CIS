import requests

torneo = "CIS2020"
alternativa = "CSI2020"
partecipanti = {
                "abruzzo": "https://api.chess.com/pub/club/team-abruzzo",
                "basilicata": "https://api.chess.com/pub/club/team-basilicata",
                "calabria": "https://api.chess.com/pub/club/team-calabria",
                "campania": "https://api.chess.com/pub/club/team-napoli-campania",
                "emilia": "https://api.chess.com/pub/club/team-emilia-romagna",
                "friuli": "https://api.chess.com/pub/club/udine-e-fvg",
                "lazio": "https://api.chess.com/pub/club/lazio",
                "lombardia": "https://api.chess.com/pub/club/i-lumbard",
                "piemonte": "https://api.chess.com/pub/club/team-piemonte",
                "sicilia": "https://api.chess.com/pub/club/team-sicilia",
                "toscana": "https://api.chess.com/pub/club/team-toscana",
                "trentino": "https://api.chess.com/pub/club/team-trentino-sudtirol",
                "veneto": "https://api.chess.com/pub/club/team-veneto"
                }


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
                    print("\033[32m" + "(Vinta) " + avversario.get("name"))
                if risultato == "lose":
                    print("\033[31m" + "(Persa) " + avversario.get("name"))
                if risultato == "draw":
                    print("\033[37m" + "(Patta) " + avversario.get("name"))
                if risultato is None:
                    print("\033[37m" + "(In corso) " + avversario.get("name"))

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


for nome, api in partecipanti.items():
    squadra = Regione(api)
    squadra.elenco_risultati()

