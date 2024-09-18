from selenium import webdriver
import time
import unittest
import os
import sys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages.signupPage import SignupPage
from pages.createAccountPage import CreateAccountPage

service = Service("C:\\Users\\acer\\AppData\\Roaming\\Python\\Python312\\chromedriver.exe")
class SignUp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_signUp(self):
        driver = self.driver
        driver.get("https://automationexercise.com/")

        signup = SignupPage(driver)
        signup.initialButtonClick()
        signup.enter_username("kriss")
        signup.enter_email("kriss@g.com")
        signup.signUpButtonClick()

        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__ == '__main__':
    unittest.main()

