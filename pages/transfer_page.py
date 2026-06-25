from selenium.webdriver.common.by import By


class TransferPage:

    transfer_link = (By.LINK_TEXT, "Transfer Funds")
    amount = (By.ID, "amount")
    transfer_btn = (By.XPATH, "//input[@value='Transfer']")

    def __init__(self, driver):
        self.driver = driver

    def transfer_money(self, amt):
        self.driver.find_element(*self.transfer_link).click()
        self.driver.find_element(*self.amount).send_keys(amt)
        self.driver.find_element(*self.transfer_btn).click()

    def click_transfer(self):
        pass

    def enter_amount(self, param):
        pass

    def select_from_account(self):
        pass

    def select_to_account(self):
        pass

    def submit_transfer(self):
        pass

    def click_transfer_funds(self):
        pass