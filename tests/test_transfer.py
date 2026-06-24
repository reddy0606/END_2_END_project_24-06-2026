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

from pages.login_page import LoginPage
from pages.transfer_page import TransferPage


def test_transfer(setup, registered_user):
    driver = setup

    login = LoginPage(driver)
    login.enter_username(registered_user)
    login.enter_password("Sai@123")
    login.click_login()

    transfer = TransferPage(driver)
    transfer.transfer_money("500")

    assert "Transfer Complete!" in driver.page_source