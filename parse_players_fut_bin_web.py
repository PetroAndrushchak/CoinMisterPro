from futbin.web.driver.web_driver_manager import WebDriverManager

from futbin.web.pages.players_page import PlayersPage
from selene import browser

WebDriverManager.set_up_selene_driver()

players_page = PlayersPage()

if browser.driver.current_url != "https://www.futbin.com/players":
    browser.driver.get("https://www.futbin.com/players")

# Wait for page to load
while browser.driver.execute_script("return document.readyState") != "complete":
    print("Waiting for page to load")

players = players_page.parse_players_displayed_on_page()

total_number_of_pages = players_page.get_total_number_of_pages()
print("dsfsdf")
