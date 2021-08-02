from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException , NoSuchElementException , ElementClickInterceptedException , WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

google_chrome_options = Options()
#
# google_chrome_options.add_argument('--headless')
google_chrome_options.add_argument("--mute-audio")
google_chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(executable_path='D:\Devendra\chromedriver\chromedriver.exe' , options=google_chrome_options)
# driver = webdriver.Chrome(executable_path='D:\Devendra\chromedriver\chromedriver.exe')
# driver = webdriver.Firefox(executable_path=r'D:\Devendra\chromedriver\geckodriver.exe')

driver.get("https://web.whatsapp.com")

driver.implicitly_wait(15)

status_button = driver.find_element_by_css_selector("#side > header > div._3yZPA > div > span > div._2cNrC > div._26lC3")

status_button.click()

driver.implicitly_wait(10)

action = ActionChains(driver)




users = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, " div.statusList > div > span > div > div > div._3OvU8 > div._3vPI2 > div.zoWT4 ")))

user_list = []
count = 0

for user in users:
    user_list.append(user.text)

print(user_list)

for user_get in user_list:
    print(user_get)
    try:
        user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH ,"//span[@title='{}']".format(user_get))))
        # WebDriverWait(driver, 10)
        user.click()
        time.sleep(1)
        print("hey clicked")

        status_count = driver.find_elements_by_css_selector("div.sZBni")
        print(len(status_count))

        for status in status_count:
            if len(status_count) <= 1:
                video = WebDriverWait(driver , 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div._19K91 > video")))
                print("the content", video)

                if video:
                    for videos in video:
                        print(videos.get_attribute("src"))

                status_close = driver.find_element_by_css_selector("button.z4GOz")
                status_close.click()
                status_button1 = driver.find_element_by_css_selector("#side > header > div._3yZPA > div > span > div._2cNrC > div._26lC3")
                status_button1.click()
            else:
                print("i am working in more")
                video = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div._19K91 > video")))
                if video:
                    for videos in video:
                        print(videos.get_attribute("src"))
                        next = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div._1ADa8._3Nsgw.app-wrapper-web.font-fix.os-win > span:nth-child(3) > div._3bvta > span > div:nth-child(2) > div > div.XzUO1")))
                        next.click()
                        driver.implicitly_wait(5)
                status_close = driver.find_element_by_css_selector("button.z4GOz")
                status_close.click()
                status_button1 = driver.find_element_by_css_selector(
                    "#side > header > div._3yZPA > div > span > div._2cNrC > div._26lC3")
                status_button1.click()


    except TimeoutException:
        print("Its not finding the time")


    except NoSuchElementException :
        print("Element not Found")

    except ElementClickInterceptedException:
        print("Internet is very slow ")

    except WebDriverException :
        print("Chrome not reachable")


driver.close()
