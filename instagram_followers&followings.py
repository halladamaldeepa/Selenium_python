import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.instagram.com/guviofficial/")
time.sleep(15)
ul=driver.find_element(By.TAG_NAME,"ul")
item=ul.find_elements(By.TAG_NAME,"li")
for i in item:
    print(i.text)
driver.quit()