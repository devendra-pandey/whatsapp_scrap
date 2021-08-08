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

chrome_options = Options()


# chrome_options.add_experimental_option("debuggerAddress","localhost:8989")
#
# google_chrome_options.add_argument('--headless')
chrome_options.add_argument("--mute-audio")

# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--enable-logging')
chrome_options.add_argument('--log-level=0')
# chrome_options.add_argument('--single-process')

path_ubuntu = "/media/devendra/Development/scrapping/Whatsapp/Whatsapp/chromedriver/chromedriver"

path_wind = "D:\Devendra\chromedriver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=path_ubuntu , options=chrome_options)
# driver = webdriver.Chrome(executable_path='D:\Devendra\chromedriver\chromedriver.exe')
# driver = webdriver.Firefox(executable_path=r'D:\Devendra\chromedriver\geckodriver.exe')

driver.get("https://web.whatsapp.com")

driver.implicitly_wait(15)
try:
    status_button = driver.find_element_by_css_selector("#side > header > div._3yZPA > div > span > div._2cNrC > div._26lC3")

    status_button.click()

    driver.implicitly_wait(10)

    action = ActionChains(driver)

    users = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, " div.statusList > div > span > div > div > div._3OvU8 > div._3vPI2 > div.zoWT4 ")))

    user_list = []

    story = []

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

            if len(status_count) <= 1:
                driver.implicitly_wait(2)

                if driver.find_element_by_css_selector("div._19K91"):
                    src = driver.find_element_by_css_selector("div._19K91")
                    try:
                        if src.find_element_by_tag_name('img'):
                            image = src.find_element_by_tag_name('img').get_attribute("src")
                            print(image)
                            story.append(image)
                    except NoSuchElementException:
                        video = src.find_element_by_tag_name('video').get_attribute("src")
                        print(video)
                        story.append(video)
                else:
                    pass
                status_close = driver.find_element_by_xpath('//button[@class="z4GOz"]')
                print("close the status single")
                status_close.click()
                status_button1 = driver.find_element_by_css_selector(
                    "#side > header > div._3yZPA > div > span > div._2cNrC > div._26lC3")
                status_button1.click()
            else:
                for status_click in status_count:
                    driver.implicitly_wait(5)
                    if driver.find_element_by_css_selector("div._19K91"):
                        src = driver.find_element_by_css_selector("div._19K91")
                        try:
                            if src.find_element_by_tag_name('img'):
                                image = src.find_element_by_tag_name('img').get_attribute("src")
                                print(image)
                                story.append(image)
                        except NoSuchElementException:
                            video = src.find_element_by_tag_name('video').get_attribute("src")
                            print(video)
                            story.append(video)
                    else:
                        pass
                    next = driver.find_element_by_xpath('//div[@class="XzUO1"]')
                    next.click()
                status_close = driver.find_element_by_xpath('//button[@class="z4GOz"]')
                print("close the status of the multiple")
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
            status_close = driver.find_element_by_xpath('//button[@class="z4GOz"]')
            status_close.click()
            status_button1 = driver.find_element_by_css_selector(
                "#side > header > div._3yZPA > div > span > div._2cNrC > div._26lC3")
            status_button1.click()

        except WebDriverException :
            print("Chrome not reachable")
            status_close = driver.find_element_by_xpath('//button[@class="z4GOz"]')
            status_close.click()
            status_button1 = driver.find_element_by_css_selector(
                "#side > header > div._3yZPA > div > span > div._2cNrC > div._26lC3")
            status_button1.click()

except NoSuchElementException:
    print("No element Found")

print(story)


driver.close()

