from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://duckduckgo.com/")

#add wait for 10 sec
driver.implicitly_wait(10)
search_box = driver.find_element(By.NAME,"q")

search_box.send_keys("selenium")

#press enter key to submit the search string
search_box.send_keys(Keys.RETURN)
print("implicit wait executed successfully")
driver.quit()