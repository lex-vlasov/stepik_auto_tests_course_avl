from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))

    button = browser.find_element(By.ID,'book')
    button.click()

    x = int(browser.find_element(By.ID, 'input_value').text)
    result = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(result)

    time.sleep(1)

    button2 = browser.find_element(By.ID, 'solve')
    button2.click()

finally:
    time.sleep(7)
    browser.quit()