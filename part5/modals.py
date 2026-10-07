#------------------simple modal-----------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


# driver = webdriver.Chrome()
# driver.maximize_window()

# driver.get("https://practice-automation.com/modals/")
# modal_btn = driver.find_element(By.ID,"simpleModal").click()
# time.sleep(3)

# modal_title = driver.find_element(By.ID,"pum_popup_title_1318").text
# print(f"Model Title:{modal_title}")

# modal_content= driver.find_element(By.XPATH,"(//div[@class='pum-content popmake-content'])[2]").text
# print(f"Model Title:{modal_content}")
# time.sleep(3)

# modal_close = driver.find_element(By.XPATH,"(//button[@class='pum-close popmake-close'])[2]").click()
# driver.quit()


#--------------------------form modal--------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practice-automation.com/modals/")
form_modal_btn = driver.find_element(By.ID,"formModal")

driver.execute_script("arguments[0].scrollIntoView();",form_modal_btn)
time.sleep(3)
form_modal_btn.click()

form_name =driver.find_element(By.NAME,"g1051-name").send_keys("Chetana")

form_email =driver.find_element(By.NAME,"g1051-email").send_keys("Chetana@gmail.com")

form_message =driver.find_element(By.XPATH,"//textarea[@id='contact-form-comment-g1051-message']").send_keys("I am A software tester at fixing dots")
time.sleep(5)

form_submit = driver.find_element(By.XPATH,'(//button[@type="submit"])[2]')
form_submit.click()
print("form submitted successfully")
driver.quit()
