from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()

driver.get("https://bbk.fixingdots.com/")
print(driver.title)
driver.maximize_window()
time.sleep(10)

# driver.get("http://65.0.162.13/home#login")
# print(driver.title)
# time.sleep(10)
user_ele = driver.find_element(By.ID,"username")
pwd_ele = driver.find_element(By.XPATH,"//input[@id='password-field']")

print(user_ele.is_enabled())  # returns true/false
print(user_ele.is_displayed())  # returns true/false

print(pwd_ele.is_enabled())
print(pwd_ele.is_displayed())


user_ele.send_keys("tester@fixingdotscom")
pwd_ele.send_keys("Open@1234")
time.sleep(5)
driver.find_element(By.XPATH,"//button[normalize-space()='sign in']").click()
time.sleep(5)

driver.quit()