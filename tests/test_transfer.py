# from pages.login_page import LoginPage
# from pages.transfer_page import TransferPage
#
#
# def test_transfer(setup):
#     driver = setup
#
#     login = LoginPage(driver)
#     login.enter_username("sai12345")
#     login.enter_password("Sai@123")
#     login.click_login()
#
#     transfer = TransferPage(driver)
#     transfer.transfer_money("500")
#
#     assert "Transfer Complete!" in driver.page_source

# from pages.login_page import LoginPage
# from pages.transfer_page import TransferPage
# from tests.test_register import created_user
#
#
# def test_transfer(setup):
#     driver = setup
#
#     login = LoginPage(driver)
#     login.enter_username(created_user)
#     login.enter_password("Sai@123")
#     login.click_login()
#
#     transfer = TransferPage(driver)
#     transfer.transfer_money("500")
#
#     assert "Transfer Complete!" in driver.page_source

# from pages.login_page import LoginPage
# from pages.transfer_page import TransferPage
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# def test_transfer(setup, registered_user):
#     driver = setup
#
#     login = LoginPage(driver)
#     login.enter_username(registered_user["username"])
#     login.enter_password(registered_user["password"])
#     login.click_login()
#
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Transfer Funds"))
#     )
#
#     transfer = TransferPage(driver)
#     transfer.click_transfer()


import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


def test_transfer(setup):
    driver = setup

    # Login with valid demo account
    login = LoginPage(driver)

    login.enter_username("john")
    login.enter_password("demo")
    login.click_login()

    # Wait for dashboard
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Transfer Funds"))
    )

    # Open transfer page
    driver.find_element(By.LINK_TEXT, "Transfer Funds").click()

    # Enter amount
    driver.find_element(By.ID, "amount").send_keys("100")

    # Click transfer button
    driver.find_element(By.XPATH, "//input[@value='Transfer']").click()

    # Validate success
    assert "Transfer Complete!" in driver.page_source