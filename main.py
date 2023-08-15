import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://dash.zeabur.com/login")
driver.find_element(By.LINK_TEXT, "Sign in with Github").click()
driver.find_element(By.ID, "login_field").sendkeys(os.environ['USERNAME'])
driver.find_element(By.ID, "password").sendkeys(os.environ['PASSWORD'])
driver.find_element(By.NAME, "commit").click()
driver.find_element(By.LINK_TEXT, "Days").click()
driver.find_element(By.LINK_TEXT, "Extend Trial").click()

time.sleep(10)

driver.quit()