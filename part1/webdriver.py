from selenium import webdriver
import time 

driver = webdriver.Chrome()

driver.get("https://google.com")
print(driver.title)

#print(driver.current_url)
#driver.fullscreen_window()

driver.maximize_window()
# driver.minimize_window()
time.sleep(10)
driver.quit()


