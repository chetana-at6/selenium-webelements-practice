from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
time.sleep(4)
dropdown = driver.find_element(By.CLASS_NAME,"search-box")

driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
time.sleep(3)
dropdown.click()

dropdown.send_keys('s')
option = driver.find_element(By.XPATH,"//div[normalize-space()='SUV']")
#option = driver.find_element(By.XPATH,"//div[@class='searchable-option' and text()='SUV']")
option.click()

time.sleep(3)
driver.quit()