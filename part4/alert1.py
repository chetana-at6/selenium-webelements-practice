from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.guru99.com/V4/index.php")
time.sleep(3)

login_btn  = driver.find_element(By.NAME,"btnLogin")
login_btn.click()
time.sleep(3)

alert = driver.switch_to.alert  # switch focus to alert window
time.sleep(3)

print("Alert message:",alert.text)
alert.accept()

time.sleep(3)
driver.quit()