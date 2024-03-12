from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")
#browser.get('http://suninjuly.github.io/cats.html')

#time.sleep(2)

button = browser.find_element(By.ID, "verify")
#button = browser.find_element(By.ID, "button")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text