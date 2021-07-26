from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome(executable_path='/media/devendra/Development/scrapping/Whatsapp/chromedriver/chromedriver')
driver.get("https://web.whatsapp.com")

driver.implicitly_wait(15)

status_button = driver.find_element_by_css_selector("#side > header > div._3yZPA > div > span > div > div")

status_button.click()



