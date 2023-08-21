import requests

class FutBin:

    PLAYERS_PAGE = 'https://www.futbin.com/players'

    def players_page(self):
        response = requests.get(self.PLAYERS_PAGE)
        response.raise_for_status()

