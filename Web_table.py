import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

#total number of rows and columns in table
no_of_rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
no_of_cols=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print("no. of rows in table are: ",no_of_rows)
print("no. of cols in table are: ",no_of_cols)

#retrieving specific data from table
data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[3]")
print(data.text)

#retrieving all data from table
for r in range(2,no_of_rows+1):
    for c in range(1,no_of_cols+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]")
        print(data.text,end='             ')
    print()


#read data based on condition
for r in range(2,no_of_rows+1):
    author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author_name=="Mukesh":
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price= driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(book_name,"  ",author_name,"  ",price   )



driver.quit()
