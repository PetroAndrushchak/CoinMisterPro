
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--remote-debugging-port=9222')
#
# chrome_options.add_experimental_option("detach", True)

# #Sample Python Code
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

service = ChromeService()
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://www.example.com')
