from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    btBook  = browser.find_element_by_id("book")
    btBook.click()

    browser.execute_script("return arguments[0].scrollIntoView(true);", btBook)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    edAnswer = browser.find_element_by_id("answer")
    edAnswer.send_keys(y)

    btnSolve = browser.find_element_by_id("solve")
    btnSolve.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()