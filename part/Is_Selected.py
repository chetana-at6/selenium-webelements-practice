from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://65.0.162.13:8000/home")
print(driver.title)
driver.fullscreen_window()
time.sleep(6)


user_ele = driver.find_element(By.XPATH, "//input[@id='userName']")
pwd_ele = driver.find_element(By.XPATH, "//input[@id='password']")

user_ele.send_keys("sharmasneha0740@gmail.com")
pwd_ele.send_keys("Ankit@2003")
time.sleep(5)
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(10)
driver.get("http://65.0.162.13:8000/panel/dashboard")
time.sleep(10)
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"//a[.//span[text()='Role']]").click()
time.sleep(5)
driver.quit()