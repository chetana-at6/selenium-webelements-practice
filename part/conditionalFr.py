from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://65.0.162.13/home")
print(driver.title)
driver.fullscreen_window()
time.sleep(6)

driver.find_element(By.XPATH, "//*[@id='navbarSupportedContent']/ul/li[4]/a").click()
time.sleep(5)

user_ele = driver.find_element(By.XPATH,"//input[@id='userName']")
pwd_ele = driver.find_element(By.XPATH,"//input[@id='password']")

print(user_ele.is_displayed())
print(user_ele.is_enabled())

print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("sharmasneha0740@gmail.com")
pwd_ele.send_keys("Ankit@2003")
time.sleep(5)
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(10)
driver.get("http://65.0.162.13/panel/dashboard")
time.sleep(10)
driver.maximize_window()
driver.get("http://65.0.162.13/panel/roles")
time.sleep(15)
driver.quit()