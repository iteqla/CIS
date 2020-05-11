import requests
torneo = "CIS2020"

class Elenco_partite:
    def __init__(self, nome, request):
        self.nome = nome
        self.request = request
        self.tutte = request.json()
        self.finite = self.tutte["finished"]

    def elenco(self):
        print("\n===== Elenco partite " + self.nome + " =====")
        for x in self.finite:
            titolo = x.get("name")
            risultato = x.get("result")
            if torneo in titolo:
                print(titolo, risultato)


toscana = Elenco_partite("Toscana", requests.get("https://api.chess.com/pub/club/team-toscana/matches"))
toscana.elenco()

abruzzo = Elenco_partite("Abruzzo", requests.get("https://api.chess.com/pub/club/team-abruzzo/matches"))
abruzzo.elenco()

emilia = Elenco_partite("Emilia-Romagna", requests.get("https://api.chess.com/pub/club/team-emilia-romagna/matches"))
emilia.elenco()

calabria = Elenco_partite("Calabria", requests.get("https://api.chess.com/pub/club/team-calabria/matches"))
calabria.elenco()

basilicata = Elenco_partite("Basilicata", requests.get("https://api.chess.com/pub/club/team-basilicata/matches"))
basilicata.elenco()

sicilia = Elenco_partite("Sicilia", requests.get("https://api.chess.com/pub/club/team-sicilia/matches"))
sicilia.elenco()

# def toscana_elenco_partite():
#     all_matches = requests.get("https://api.chess.com/pub/club/team-toscana/matches")
#     partite = all_matches.json()
#     finite = partite["finished"]
#     print("\n===== Elenco partite Toscana =====")
#     for x in finite:
#         titolo = x.get("name")
#         risultato = x.get("result")
#         if torneo in titolo:
#             print(titolo, risultato)
#
#
#
# def abruzzo_elenco_partite():
#     r = requests.get("https://api.chess.com/pub/club/team-abruzzo/matches")
#     partite = r.json()
#     finite = partite["finished"]
#     print("\n===== Elenco partite Abruzzo =====")
#     for x in finite:
#         titolo = x.get("name")
#         risultato = x.get("result")
#         if torneo in titolo:
#             print(titolo, risultato)
#
# toscana_elenco_partite()
# abruzzo_elenco_partite()