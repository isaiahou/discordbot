import os
import discord
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# COMMANDS FOR RUNNING LOCALLY
# from dotenv import load_dotenv

service = Service(os.environ.get('CHROMEDRIVER_PATH'))
chrome_options = Options()
# Remove this line if running locally.
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service = service, options = chrome_options)

# COMMANDS FOR RUNNING LOCALLY
# load_dotenv()
username = os.environ.get('LC_USER')
password = os.environ.get('LC_PASS')

class ProblemFinder:

    def __init__(self, difficulty = "easy"):
        self.difficulty = difficulty.upper()

    def find_problem(self):
        link = "https://leetcode.com/problemset/all/?difficulty={}&page=1".format(self.difficulty)
        driver.get(link)
        next_link = driver.find_element(By.XPATH, '//span[text()="Pick One"]')
        next_link.click()
        try:
            try:
                user_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'login')))
                user_element.send_keys(username)
                password_element = driver.find_element(By.NAME, 'password')
                password_element.send_keys(password)
                driver.find_element(By.CSS_SELECTOR, '.btn-content__2V4r').click()
                information = []
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.content__u3I1.question-content__JfgR p')))
                information.append(driver.title)
                information.append(driver.current_url)
                information.append(element.text)
                return information
            except:
                information = []
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.content__u3I1.question-content__JfgR p')))
                information.append(driver.title)
                information.append(driver.current_url)
                information.append(element.text)
                return information
        except:
            print("There was an error.")

    def find_daily(self):
        link = "https://leetcode.com/problemset/all/"
        driver.get(link)
        next_link = driver.find_element(By.XPATH, '//div[@role="cell"]/a').get_attribute('href')
        next_link.click()
        try:
            try:
                user_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'login')))
                user_element.send_keys(username)
                password_element = driver.find_element(By.NAME, 'password')
                password_element.send_keys(password)
                driver.find_element(By.CSS_SELECTOR, '.btn-content__2V4r').click()
                information = []
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.content__u3I1.question-content__JfgR p')))
                difficulty = driver.find_element(By.CLASS_NAME, 'diff').text
                information.append(driver.title)
                information.append(driver.current_url)
                information.append(element.text)
                information.append(difficulty)
                return information
            except:
                information = []
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.content__u3I1.question-content__JfgR p')))
                difficulty = driver.find_element(By.CLASS_NAME, 'diff').text
                information.append(driver.title)
                information.append(driver.current_url)
                information.append(element.text)
                information.append(difficulty)
                return information
        except:
            print("There was an error.")
