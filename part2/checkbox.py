from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/checkboxes")

# checkbox1 = driver.find_element(By.XPATH,'//input[1]')
# if not checkbox1.is_selected():
#   checkbox1.click()

# checkbox2 = driver.find_element(By.XPATH,'//input[2]')
# if not checkbox2.is_selected():
#    checkbox2.click()


# print("is checkbox1:",checkbox1.is_selected())
# print("is checkbox1:",checkbox2.is_selected())

#multiple checkbox selection
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()

time.sleep(5)
driver.quit()  