from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()


driver.get("http://uitestingplayground.com/alerts")
time.sleep(3)

#find alert button
# alert_btn = driver.find_element(By.ID,"alertButton")
# alert_btn.click()
# time.sleep(3)

# alert_btn = driver.switch_to.alert
# print("Alert message:",alert_btn.text)
# alert_btn.accept()
# print("alert is accepted")
# time.sleep(3)
# driver.quit()

#---------------confirmation alert----------------

# confirm_alert = driver.find_element(By.ID,"confirmButton")
# confirm_alert.click()
# time.sleep(3)

# confirm_alert = driver.switch_to.alert
# print("Alert message:",confirm_alert.text)
# confirm_alert.accept()
# # confirm_alert.dismiss()
# time.sleep(3)


# second_alert = driver.switch_to.alert
# print("Alert message:",second_alert.text)
# second_alert.accept()
# driver.quit()

#--------------prompt alert------------

prompt_alert = driver.find_element(By.ID,"promptButton")
prompt_alert.click()
time.sleep(3)

prompt_alert = driver.switch_to.alert
print("Alert message:",prompt_alert.text)
time.sleep(3)

prompt_alert.send_keys("hello selenium")
print("Entered text in prompt alert.")
time.sleep(3)
 
prompt_alert.accept()
#prompt_alert.dismiss()
time.sleep(3)

second_alert = driver.switch_to.alert
print("Alert message:",second_alert.text)
second_alert.accept()
driver.quit()


time.sleep(3)
driver.quit()