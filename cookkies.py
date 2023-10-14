from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
cookie=driver.get_cookies()
print("length of cookie before login",len(cookie))
print("cookies before login: ",cookie)

#login
driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

cookie=driver.get_cookies()
print("length of cookie after login: ",len(cookie))
print("cookies after login",cookie)

#adding new cookies 
cookie={'name':'my_cookie','value':'12345'}
driver.add_cookie(cookie)

#logout
driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
driver.find_element(By.XPATH,'//a[@href="/web/index.php/auth/logout"]').click()  #logout

