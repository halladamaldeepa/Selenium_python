import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.deadlinkcity.com/")
alllinks=driver.find_elements(By.TAG_NAME,'a')
print(len(alllinks))
count=0
for link in alllinks:
   url= link.get_attribute("href")
   res=requests.head(url)
   if res.status_code>=400:
       print(url," is broken link")
   else:
       print(url," is valid link ")
print("total no of links",count)
driver.quit()