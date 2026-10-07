from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://duckduckgo.com/")

search_box = driver.find_element(By.NAME,"q")
wait= WebDriverWait(driver, timeout=10)

search_box.send_keys("selenium")

search_box.send_keys(Keys.RETURN)
driver.quit()