import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("https://dash.zeabur.com/login")

driver.find_element(By.LINK_TEXT, "Sign in with Github").click()
driver.find_element(By.ID, "login_field").sendkeys(os.environ['USERNAME'])
driver.find_element(By.ID, "password").sendkeys(os.environ['PASSWORD'])
driver.find_element(By.NAME, "commit").click()
driver.find_element(By.LINK_TEXT, "Days").click()
driver.find_element(By.LINK_TEXT, "Extend Trial").click()

time.sleep(10)

driver.quit()