from selenium import webdriver
import time 
import math
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    new_window = browser.window_handles[1] #получаем имя нового окна
    browser.switch_to.window(new_window) #переходим в новое окно
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
