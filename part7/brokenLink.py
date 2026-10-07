from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests


driver = webdriver.Chrome()
driver.maximize_window()

# driver.get("https://practice.expandtesting.com/")
driver.get("http://www.deadlinkcity.com/")

time.sleep(3)

# links = driver.find_elements(By.TAG_NAME,"a")
links = driver.find_elements(By.XPATH,"//a")
# print(f"total tink found:{len(links)}")

# for link in links:
#     url = link.get_attribute("href")
#     response = requests.head(url)

# if response.status_code >=400:
#     print("broken link")
# else:
#     print("valid link") 

#links = driver.find_elements(By.TAG_NAME, "a")
links = driver.find_elements(By.XPATH,"//a")
print(f"Total links found: {len(links)}")

for link in links:
    # Get the URL from the 'href' attribute of the <a> tag
    url = link.get_attribute("href")

    # Make an HTTP HEAD request to the given URL
    try:
        response = requests.head(url, timeout=5)
        if response.status_code >= 400:
            print("Broken Link")
        else:
            print("Valid Link")
    # except:
    #     None
    except Exception as e:
             print(f"Error happened: {e}")
time.sleep(9)
driver.quit()
