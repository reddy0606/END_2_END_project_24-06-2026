import random
from selenium.webdriver.common.by import By


class RegisterPage:

    register_link = (By.LINK_TEXT, "Register")
    first_name = (By.ID, "customer.firstName")
    last_name = (By.ID, "customer.lastName")
    address = (By.ID, "customer.address.street")
    city = (By.ID, "customer.address.city")
    state = (By.ID, "customer.address.state")
    zip_code = (By.ID, "customer.address.zipCode")
    phone = (By.ID, "customer.phoneNumber")
    ssn = (By.ID, "customer.ssn")
    username = (By.ID, "customer.username")
    password = (By.ID, "customer.password")
    confirm = (By.ID, "repeatedPassword")
    submit = (By.XPATH, "//input[@value='Register']")

    def __init__(self, driver):
        self.driver = driver

    def register_user(self, username):
        unique_user = "sai" + str(random.randint(1000, 9999))

        self.driver.find_element(*self.register_link).click()

        self.driver.find_element(*self.first_name).send_keys("Sai")
        self.driver.find_element(*self.last_name).send_keys("Kumar")
        self.driver.find_element(*self.address).send_keys("Hyderabad")
        self.driver.find_element(*self.city).send_keys("Hyderabad")
        self.driver.find_element(*self.state).send_keys("Telangana")
        self.driver.find_element(*self.zip_code).send_keys("500001")
        self.driver.find_element(*self.phone).send_keys("9876543210")
        self.driver.find_element(*self.ssn).send_keys("123456")
        self.driver.find_element(*self.username).send_keys(username)

        # self.driver.find_element(*self.username).send_keys(unique_user)
        self.driver.find_element(*self.password).send_keys("Sai@123")
        self.driver.find_element(*self.confirm).send_keys("Sai@123")

        self.driver.find_element(*self.submit).click()

        # return unique_user