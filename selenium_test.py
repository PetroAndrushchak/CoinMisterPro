from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


service = ChromeService(ChromeDriverManager(version="114.0.5735.90").install())

options = Options()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.etemkeskin.com/")