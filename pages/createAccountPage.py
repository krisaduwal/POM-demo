import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locator import Locators

class CreateAccountPage():

    def __init__(self, driver):
        self.driver = driver

        self.title_id = Locators.title_id
        self.password_id = Locators.password_id
        self.dayBox_id = Locators.dayBox_id
        self.monthBox_id = Locators.monthBox_id
        self.yearBox_id = Locators.yearBox_id
        self.checkBox1_id = Locators.checkBox1_id
        self.checkBox2_id = Locators.checkBox2_id

        self.firstname_id = Locators.firstname_id
        self.lastname_id = Locators.lastname_id
        self.company_id = Locators.company_id
        self.address1_id = Locators.address1_id
        self.address2_id = Locators.address2_id
        self.country_id = Locators.country_id
        self.state_id = Locators.state_id
        self.city_id = Locators.city_id
        self.zipcode_id = Locators.zipcode_id
        self.mobNum_id = Locators.mobNum_id
        self.createAccButton_id = Locators.createAccButton_id
        self.accCreated_id = Locators.accCreated_id
        self.continueB_id = Locators.continueB_id

    def title(self):
        self.driver.find_element(By.ID, self.title_id).click()
        time.sleep(2)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_id).send_keys(password)
        time.sleep(1)

    def choose_day(self, day):
        # selectDay = self.selectDay
        self.selectDay = self.driver.find_element(By.XPATH, self.dayBox_id)
        select = Select(self.selectDay)
        select.select_by_value(day)
        time.sleep(2)

    def choose_month(self, month):
        self.selectMonth = self.driver.find_element(By.XPATH, self.monthBox_id)
        select = Select(self.selectMonth)
        select.select_by_value(month)
        time.sleep(1)

    def choose_year(self, year):
        self.selectYear = self.driver.find_element(By.XPATH, self.yearBox_id)
        select = Select(self.selectYear)
        select.select_by_value(year)
        time.sleep(1)

    def checkboxes(self):
        self.driver.find_element(By.XPATH, self.checkBox1_id).click()
        self.driver.find_element(By.XPATH, self.checkBox2_id).click()
        time.sleep(1)

    def enter_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.firstname_id).send_keys(firstname)
        time.sleep(2)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.lastname_id).send_keys(lastname)
        time.sleep(1)

    def enter_company(self, company):
        self.driver.find_element(By.XPATH, self.company_id).send_keys(company)
        time.sleep(2)

    def enter_address1(self, address1):
        self.driver.find_element(By.XPATH, self.address1_id).send_keys(address1)
        time.sleep(1)

    def enter_address2(self, address2):
        self.driver.find_element(By.XPATH, self.address2_id).send_keys(address2)
        time.sleep(1)

    def choose_country(self, country):
        self.selectCountry = self.driver.find_element(By.XPATH, self.country_id)
        select = Select(self.selectCountry)
        select.select_by_value(country)
        time.sleep(1)

    def enter_state(self, state):
        self.driver.find_element(By.XPATH, self.state_id).send_keys(state)
        time.sleep(1)

    def enter_city(self, city):
        self.driver.find_element(By.XPATH, self.city_id).send_keys(city)
        time.sleep(2)

    def enter_zipcode(self, zip):
        self.driver.find_element(By.XPATH, self.zipcode_id).send_keys(zip)
        time.sleep(1)

    def enter_number(self, phone):
        self.driver.find_element(By.XPATH, self.mobNum_id).send_keys(phone)
        time.sleep(1)

    def createButtonClick(self):
        self.driver.find_element(By.XPATH, self.createAccButton_id).click()
        time.sleep(2)

    def verify_account(self):
        try:
            print("hello")
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.accCreated_id))
            )
            print("element found")
            title = element.text
            print(f"Element text: {title}")
            assert "congratulations" in title.lower()
            print("account created successfully")
            time.sleep(2)
            print("success")
            self.driver.find_element(By.XPATH, self.continueB_id).click()

        except TimeoutException:
            print("Element not found within the given time.")
        except AssertionError:
            print(f"Assertion failed. Expected 'congratulations', but got '{title}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        time.sleep(60)