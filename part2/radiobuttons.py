from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://dmytro-ch21.github.io/')
time.sleep(3)
driver.find_element(By.XPATH,"//a[normalize-space()='Go to Dropdowns']").click()
#driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

driver.maximize_window()
ford = driver.find_element(By.ID,"radio1")


Tesla = driver.find_element(By.ID,"radio4")
Tesla.click()
bmw = driver.find_element(By.ID,"radio2")

print("ford:",ford.is_selected())
print("bmw:",bmw.is_selected())
print("Tesla:",Tesla.is_selected())

time.sleep(5)
driver.quit()