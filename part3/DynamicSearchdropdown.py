from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.co.in/")
time.sleep(4)

search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("selenium")
time.sleep(3)

suggestions = driver.find_elements(By.XPATH,"//ul[@role='listbox']//li")

for suggestion in suggestions:
    print(suggestion.text)

time.sleep(4)
driver.quit()