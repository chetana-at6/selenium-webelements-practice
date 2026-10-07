from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.maximize_window

driver.get("https://dmytro-ch21.github.io/html/web-elements.html")
multi_select = Select(driver.find_element(By.ID,"multiSelect"))

if multi_select.is_multiple:
    print("dropdown is multi select")
else:
    print("dropdown is not multi select")

multi_select.select_by_visible_text("Volvo")
multi_select.select_by_visible_text("Audi")
multi_select.select_by_visible_text("Saab")
time.sleep(3)

multi_select.deselect_by_visible_text("Volvo")
time.sleep(3)

# returns all selected options
selected_options = multi_select.all_selected_options
for option in selected_options:
    print("Selected:", option.text)

multi_select.deselect_all()
time.sleep(2)

#print all the options of dropdowns
print("all options in multi select dropdown")
allOptions = multi_select.options

for option in allOptions:
    print(option.text)
driver.close()