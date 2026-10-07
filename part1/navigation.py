from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://65.0.162.13:8000/home")
print(driver.title)

driver.maximize_window()
time.sleep(10)

driver.forward()
driver.get("http://65.0.162.13:8000/home#services")
time.sleep(10)
print(driver.title)

# driver.forward("http://65.0.162.13:8000/home#enquiry")
# print(driver.title)
# time.sleep(3)

driver.back()
driver.get("https://google.com")

driver.refresh()
driver.quit()
