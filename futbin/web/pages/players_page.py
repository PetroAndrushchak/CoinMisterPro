from selene import have
from selene.core import query
from selene.support.shared.jquery_style import ss
from futbin.models.fut_bin_raw_player import FutBinRawPlayer
import bs4
import re


class PlayersPage:

    def __init__(self):
        self.pagination_buttons = ss("li[class *='page-item' ] a:not(a[aria-label='Next'])")
        self.players_table_rows = ss("tr[class *='player_tr']")

    def get_total_number_of_pages(self):
        self.pagination_buttons.should(have.size_greater_than(1))
        pagination_buttons_with_integer_value = filter(lambda x: x.get(query.text).isdigit(), self.pagination_buttons)
        page_numbers = map(lambda x: int(x.get(query.text)), pagination_buttons_with_integer_value)
        return max(page_numbers)

    def parse_players_displayed_on_page(self):
        self.players_table_rows.should(have.size_greater_than(1))
        players = []
        for player_row in self.players_table_rows:
            parsed_player = self.parse_player_row(player_row)
            players.append(parsed_player)

        return players

    def parse_player_row(self, player_row):
        print("Parsing player from row")
        player = FutBinRawPlayer()
        player_raw_element_html = player_row.get(query.inner_html)
        soup = bs4.BeautifulSoup(player_raw_element_html, 'html.parser')

        player_name_element = soup.select("a[class *='player_name_players']")[0]
        player_name = player_name_element.get_text()

        player_id = self.get_player_id_from_player_name_link(player_name_element.get("href"))

        player_club_link_element = soup.select("a[href *='&club']")[0]
        club_id = self.get_player_club_id_from_player_club_link(player_club_link_element.get("href"))
        club_name = player_club_link_element.get("data-original-title")

        nation_id_element = soup.select("a[href *='&nation']")[0]
        nation_id = self.get_player_nation_id_from_player_nation_link(nation_id_element.get("href"))
        nation_name = nation_id_element.get("data-original-title")

        league_id_element = soup.select("a[href *='&league']")[0]
        league_id = self.get_player_league_id_from_player_league_link(league_id_element.get("href"))
        league_name = league_id_element.get("data-original-title")

        rating = soup.select("span.rating")[0].get_text()

        quality_and_rarity_attr = soup.select("span.rating")[0].get("class")
        quality_and_rarity = self.get_players_quality_and_rarity(quality_and_rarity_attr)

        position_element = soup.select(".font-weight-bold")[0]
        main_position = position_element.get_text()
        other_positions_element = soup.select(".font-weight-bold + div")[0].get_text()

        if other_positions_element == "":
            other_positions = None
        else:
            other_positions = other_positions_element.split(',')

        price = soup.select("span:has(img[src *='coins'] )")[0].get_text()

        player.name = player_name
        player.id = player_id
        player.clubId = club_id
        player.clubName = club_name
        player.nationId = nation_id
        player.nationName = nation_name
        player.leagueId = league_id
        player.leagueName = league_name
        player.rating = rating
        player.qualityAndRarity = quality_and_rarity
        player.mainPosition = main_position
        player.otherPositions = other_positions
        player.priceText = price

        print("Finished parsing player from row")
        print(player)

        return player

    def get_player_id_from_player_name_link(self, path):
        pattern = r"/[0-9]+/player/([0-9]+)/[a-zA-Z]+"
        match = re.search(pattern, path)
        if match:
            return match.group(1)
        else:
            raise RuntimeError("Player id not found in player name link")

    def get_player_club_id_from_player_club_link(self, path):
        pattern = r".*&club=([0-9]+)"
        match = re.search(pattern, path)
        if match:
            return match.group(1)
        else:
            raise RuntimeError("Player club id not found in player club link")

    def get_player_nation_id_from_player_nation_link(self, path):
        pattern = r".*&nation=([0-9]+)"
        match = re.search(pattern, path)
        if match:
            return match.group(1)
        else:
            raise RuntimeError("Player nation id not found in player nation link")

    def get_player_league_id_from_player_league_link(self, path):
        pattern = r".*&league=([0-9]+)"
        match = re.search(pattern, path)
        if match:
            return match.group(1)
        else:
            raise RuntimeError("Player league id not found in player league link")

    def get_players_quality_and_rarity(self, quality_and_rarity_class_attribute):
        return quality_and_rarity_class_attribute[quality_and_rarity_class_attribute.index('ut23') + 1:]
