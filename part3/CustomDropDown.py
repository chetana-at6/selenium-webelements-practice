from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
dropdown = driver.find_element(By.ID,"custom-select")
time.sleep(3)
driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
time.sleep(6)
dropdown.click()

optionRed = driver.find_element(By.XPATH,'//div[@class="custom-options"]/div[text()="Red"]')
optionRed.click()
time.sleep(3)

dropdown.click()

optionBlue = driver.find_element(By.XPATH,'//div[@class="custom-options"]/div[text()="Blue"]')
optionBlue.click()
time.sleep(3)

driver.quit()