import requests

class APICache:
    def __init__(self):
        self.cache = {}

    def get_response(self, url):
        if url in self.cache:
            return self.cache[url]
        else:
            response = requests.get(url).json()
            self.cache[url] = response
            return response
