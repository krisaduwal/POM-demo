from selenium import webdriver
import time
import unittest

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from locators.locator import Locators


class SignupPage():

    def __init__(self, driver):
        self.driver = driver

        self.initialButton_id = Locators.initialButton_id
        self.username_id = Locators.username_id
        self.email_id = Locators.email_id
        self.signUpButton_id = Locators.signUpButton_id

    def initialButtonClick(self):
        self.driver.find_element(By.XPATH, self.initialButton_id).click()

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_id).send_keys(username)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_id).send_keys(email)

    def signUpButtonClick(self):
        self.driver.find_element(By.XPATH, self.signUpButton_id).click()


