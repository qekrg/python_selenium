from selenium import webdriver
import time 
import unittest

class test_class_name(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
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
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test reg1 OK")
        
        
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
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
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test reg2 OK")       
        
if __name__ == "__main__":
    unittest.main()



