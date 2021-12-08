from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
    input3.send_keys("1@ya.com")
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

# находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()