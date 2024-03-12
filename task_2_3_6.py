from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)

    btn1 = browser.find_element(By.CLASS_NAME,'btn-primary')
    btn1.click()

    new_browser = browser.window_handles[1]
    browser.switch_to.window(new_browser)
    time.sleep(1)
    x = int(browser.find_element(By.ID,'input_value').text)

    result = calc(x)

    answer = browser.find_element(By.ID,'answer')
    answer.send_keys(result)

    time.sleep(1)

    btn2 = browser.find_element(By.CLASS_NAME,'btn-primary')
    btn2.click()


finally:
    time.sleep(7)
    browser.quit()