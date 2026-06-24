from selenium.webdriver.common.by import By


class LoginPage:

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_btn = (By.XPATH, "//input[@value='Log In']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, uname):
        self.driver.find_element(*self.username).send_keys(uname)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()