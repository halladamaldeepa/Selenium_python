from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Deepa:

   def __init__(self, web_url):
       self.url = web_url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


   def login(self):
           self.driver.maximize_window()
           self.driver.get(self.url)
           sleep(4)
           self.driver.find_element(by=By.XPATH, value='/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a').click()
           sleep(4)
           print(self.driver.title)
           self.driver.find_element(by=By.XPATH,
                                    value='/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a').click()
           sleep(4)
           print(self.driver.title)
           windowsid=self.driver.window_handles
           parentwindowid=windowsid[0]
           childwindowid=windowsid[1]
           print("parent window id is:",parentwindowid)
           print("child window id is:",childwindowid)
           self.driver.quit()
deepa = Deepa("https://www.cowin.gov.in/")
deepa.login()
