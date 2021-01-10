from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


import time
import math
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд


    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element_by_id("book")
    k = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()
    x = browser.find_element_by_id("input_value").text
    area = browser.find_element_by_id("answer")
    area.send_keys(calc(x))
    buttons = WebDriverWait(browser, 12).until(
        EC.element_located_to_be_selected(By.ID, "solve")
    )
    buttons.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(12)
    browser.quit()
    # закрываем браузер после всех манипуляций