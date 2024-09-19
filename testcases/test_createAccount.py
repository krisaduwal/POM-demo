import unittest

from pages.createAccountPage import CreateAccountPage
from test_signup import SignUp

class CreateAccount(SignUp):


    # SignUp.setUpClass()
    @classmethod
    def setUpClass(cls):
        SignUp.setUpClass()

    def test_createAcc(self):
        self.test_signUp()

        create = CreateAccountPage(self.driver)

        create.title()
        create.enter_password("9876503210")
        create.choose_day('8')
        create.choose_month('12')
        create.choose_year('2001')
        create.checkboxes()
        create.enter_firstname("krisss")
        create.enter_lastname("rue")
        create.enter_company("fleet")
        create.enter_address1("ktm1")
        create.enter_address2("ktm2")
        create.choose_country("United States")
        create.enter_state("NY")
        create.enter_city("NYC")
        create.enter_zipcode("9876")
        create.enter_number("9876543211")
        create.createButtonClick()
        create.verify_account()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

# if __name__ == '__main__':
#     unittest.main()