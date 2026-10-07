# Install Selenium in the Python interpreter selected by your editor:
# python -m pip install selenium
# import webdriver module from selenium package
from selenium import webdriver # type: ignore
import time

from selenium.webdriver.common.by import By # type: ignore

#instantiate webdriver and launch Chrome browser
driver = webdriver.Chrome()

#maximise browser window
driver.maximize_window()

# Navigate to saucedemo website - open url
driver.get("https://www.saucedemo.com")
time.sleep(2) #wait for 2 seconds to let the page load


input_fields = driver.find_elements(By.TAG_NAME,'input')

# print(input_fields[0].get_attribute('id'))
# print(input_fields[1].get_attribute('id'))
# print(input_fields[2].get_attribute('id'))

# print(len(input_fields))

index = 0
for field in input_fields:
    print(f"Index:{index} : {field.get_attribute('id')}")
    index=index+1

input_fields[0].send_keys('standard_user')
input_fields[1].send_keys('secret_sauce')
input_fields[2].click()
time.sleep(5) 

products =driver.find_elements(By.XPATH,"//div[@class='inventory_item_name ']")

print("Product Lists")
for product in products:
    print(product.text)


driver.quit() 