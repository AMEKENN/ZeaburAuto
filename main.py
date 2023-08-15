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

driver.find_element(By.CSS_SELECTOR, "#root>div>div>div>div>div>div>a>div").click()
driver.find_element(By.ID, "login_field").sendkeys(os.environ['USERNAME'])
driver.find_element(By.ID, "password").sendkeys(os.environ['PASSWORD'])
driver.find_element(By.NAME, "commit").click()
driver.find_element(By.CSS_SELECTOR, "#root>div>div>div>div.overflow-auto>div>div>div.flex").click()
driver.find_element(By.CSS_SELECTOR, "#headlessui-dialog-panel-\:r2\:>div:nth-child(4)>div>button").click()

time.sleep(10)

driver.quit()