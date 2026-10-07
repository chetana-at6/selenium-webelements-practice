from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practice.expandtesting.com/")
time.sleep(3)

link = driver.find_element(By.LINK_TEXT,"Test Login Page")
time.sleep(3)


driver.execute_script("arguments[0].scrollIntoView(true);", link)
time.sleep(3)

link.click()

time.sleep(3)
driver.quit()