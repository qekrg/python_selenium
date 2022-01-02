from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    num1 = int(x)
    num2 = int(y)
    sum_el = num1 + num2
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text('%s' % sum_el) 
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
