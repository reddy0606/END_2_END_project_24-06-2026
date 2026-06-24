# from pages.login_page import LoginPage
# from utilities.read_data import get_data
#
#
# def test_login(setup):
#     driver = setup
#
#     data = get_data("testdata/testdata.xlsx", "LoginData")
#
#     username = data[3][0]
#     password = data[3][1]
#
#     login = LoginPage(driver)
#     login.enter_username(username)
#     login.enter_password(password)
#     login.click_login()
#
#     assert "Accounts Overview" in driver.page_source
#
#     print(driver.current_url)
#     print(driver.page_source)


# "------------------------------------------------------------"



# from pages.login_page import LoginPage
# from tests.test_register import created_user
#
#
# def test_login(setup):
#     driver = setup
#
#     login = LoginPage(driver)
#
#     login.enter_username(created_user)
#     login.enter_password("Sai@123")
#     login.click_login()
#
#     print(driver.page_source)
#
#     assert "Accounts Overview" in driver.page_source




# from pages.login_page import LoginPage
# from tests.test_register import created_user
#
#
# def test_login(setup):
#     driver = setup
#
#     login = LoginPage(driver)
#
#     login.enter_username(created_user)
#     login.enter_password("Sai@123")
#     login.click_login()
#
#     print(driver.page_source)
#
#     assert "Accounts Overview" in driver.page_source

from pages.login_page import LoginPage


def test_login(setup, registered_user):
    driver = setup

    login = LoginPage(driver)
    login.enter_username(registered_user)
    login.enter_password("Sai@123")
    login.click_login()

    assert "Accounts Overview" in driver.page_source