from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()  # Assumes chromedriver is in PATH
driver.maximize_window()

# 1. Navigate to Swag Labs login page
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# 2. Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

add_to_cart_button = driver.find_element(By.XPATH, "(//button[text()='Add to cart'])[1]")
add_to_cart_button.click()
time.sleep(10)
driver.quit()