from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
#sleep(4)
driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
#sleep(4)
driver.find_element(By.NAME,"password").send_keys("admin123")
#sleep(4)
driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
#sleep(4)
actual_title=driver.title
exp_title="OrangeHRM"

if actual_title==exp_title:
    print("login test passed")
else:
    print("login test failed")
print("current url of the webpage is:",driver.current_url)

txt=driver.page_source
print(txt)
file=open("file_deepa.txt","w")
file.write(txt)
file.close()
driver.close()
