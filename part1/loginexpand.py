
from selenium import webdriver # type: ignore

from selenium.webdriver.common.by import By # type: ignore

import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practice.expandtesting.com/login")

username = driver.find_element(By.ID,"username")
username.send_keys("practice")

password = driver.find_element(By.ID,"password")
password.send_keys("SuperSecretPassword!")

login = driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
login.click()

time.sleep(5)
driver.quit()