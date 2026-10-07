from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://dmytro-ch21.github.io/html/web-elements.html")

dropdown = Select(driver.find_element(By.ID,"carBrands"))

if dropdown.is_multiple:
    print("dropdown is multiselect")
else:
    print("dropdown is not multiselect")

dropdown.select_by_visible_text("Mercedes")
print("select option:",dropdown.first_selected_option.text)

time.sleep(2)

dropdown.select_by_value("audi")
print("select option:",dropdown.first_selected_option.text)

time.sleep(2)

dropdown.select_by_index(1)
print("select option:",dropdown.first_selected_option.text)

time.sleep(2)
driver.quit()