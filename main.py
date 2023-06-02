import datetime
from region import Region

adesso = datetime.datetime.now().replace(microsecond=0)
torneo = "CIS2023"
alternativa = "CSI2023"
partecipanti = {
    "Abruzzo": "https://api.chess.com/pub/club/team-abruzzo",
    "Basilicata": "https://api.chess.com/pub/club/team-basilicata",
    "Calabria": "https://api.chess.com/pub/club/team-calabria",
    "Emilia-Romagna": "https://api.chess.com/pub/club/team-emilia-romagna",
    "Lazio": "https://api.chess.com/pub/club/lazio",
    "Liguria": "https://api.chess.com/pub/club/team-liguria",
    "Lombardia": "https://api.chess.com/pub/club/i-lumbard",
    "Marche": "https://api.chess.com/pub/club/team-marche",
    "Piemonte": "https://api.chess.com/pub/club/team-piemonte",
    "Puglia": "https://api.chess.com/pub/club/team-puglia",
    "Sardegna": "https://api.chess.com/pub/club/sardegna",
    "Sicilia": "https://api.chess.com/pub/club/team-sicilia",
    "Toscana": "https://api.chess.com/pub/club/team-toscana",
    "Trentino-Südtirol": "https://api.chess.com/pub/club/team-trentino-sudtirol",
    "Veneto": "https://api.chess.com/pub/club/team-veneto",
    "Valle d'Aosta": "https://api.chess.com/pub/club/team-valle-daosta",
}


def print_results():
    results_file = open(str(torneo) + "_risultati" + ".txt", "w")
    results_file.write("Risultati " + str(torneo) + " aggiornati al " + str(adesso) + "\n")
    print("Risultati " + str(torneo) + " aggiornati al " + str(adesso) + "\n")

    for nome, api in partecipanti.items():
        region = Region(nome, api, torneo, alternativa)
        results = region.get_all_matches_results()
        results_text = "\n".join(results)
        results_file.write("\n===== Elenco partite " + region.name + " =====\n")
        results_file.write(results_text + "\n")
        print("\n===== Elenco partite " + region.name + " =====")
        print(results_text)

    print("\nRaccolta risultati completata per tutte le squadre partecipanti.")
    results_file.write("\nRaccolta risultati completata per tutte le squadre partecipanti.")
    results_file.close()

def main():
    print_results()


if __name__ == "__main__":
    main()
