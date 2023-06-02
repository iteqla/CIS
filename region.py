from api_cache import APICache

class Region:
    def __init__(self, name, api, torneo, alternativa):
        self.name = name
        self.api = api
        self.torneo = torneo
        self.alternativa = alternativa
        self.cache = APICache()

    def get_all_matches(self):
        response = self.cache.get_response(self.api + "/matches")
        return response.get("finished", []) + response.get("in_progress", []) + response.get("registered", [])

    def is_valid_match(self, match):
        title = match.get("name")
        return self.torneo in title or self.alternativa in title

    def get_match_result(self, match, opponent):
        result = match.get("result")
        opponent_name = opponent.get("name")
        if result == "win":
            return "(Vinta) " + opponent_name
        elif result == "lose":
            return "(Persa) " + opponent_name
        elif result == "draw":
            return "(Patta) " + opponent_name
        elif result is None:
            return "(In corso) " + opponent_name

    def get_all_matches_results(self):
        matches = self.get_all_matches()
        opponent_urls = [match.get("opponent") for match in matches]
        opponents = [self.cache.get_response(url) for url in opponent_urls]
        return [
            self.get_match_result(match, opponent)
            for match, opponent in zip(matches, opponents)
            if self.is_valid_match(match)
        ]

    def get_players(self):
        response = self.cache.get_response(self.api + "/members")
        return response.get("all_time", []) + response.get("weekly", []) + response.get("monthly", [])

    def print_players(self):
        players = self.get_players()
        usernames = [player.get("username") for player in players]
        print("\n===== Elenco giocatori " + self.name + " =====")
        print("\n".join(usernames))
