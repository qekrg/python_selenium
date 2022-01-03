from selenium import webdriver
import time 
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("2@ya.ru")
    current_dir = os.path.abspath(os.path.dirname('lesson2_2_step8.py'))# получаем путь к деректории текущего скрипта
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name) # получаем путь к file_example.txt
    element = browser.find_element_by_css_selector("[type='file']")
    element.send_keys(file_path)
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
