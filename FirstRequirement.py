from selenium import webdriver
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class LoginPageTest(unittest.TestCase):

 def  test_with_correct_password(self):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://the-internet.herokuapp.com/login")
    username="tomsmith"
    password="SuperSecretPassword!"
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_elements_by_css_selector(".fa.fa-2x.fa-sign-in")[0].click()
    sleep(2)
    success_message =driver.find_elements_by_css_selector("#flash")[0].text
    self.assertEqual(success_message, 'You logged into a secure area!\n×')

 def  test_with_incorrect_password(self):
     driver = webdriver.Chrome(ChromeDriverManager().install())
     driver.get("http://the-internet.herokuapp.com/login")
     username="tomsmith"
     password="IncorrectPassword"
     driver.find_element_by_name("username").send_keys(username)
     driver.find_element_by_name("password").send_keys(password)
     driver.find_elements_by_css_selector(".fa.fa-2x.fa-sign-in")[0].click()
     sleep(2)
     error_message =driver.find_elements_by_css_selector("#flash")[0].text
     self.assertEqual(error_message, 'Your password is invalid!\n×')    
 
if __name__ == '__main__':
    unittest.main()
