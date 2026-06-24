# from pages.register_page import RegisterPage
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# def test_register(setup):
#     driver = setup
#     reg = RegisterPage(driver)
#
#     reg.register_user()
#
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.TAG_NAME, "body"))
#     )
#
#     page_text = driver.page_source
#     print(page_text)
#
#     assert "Welcome" in page_text or "customer was created successfully" in page_text


# from pages.register_page import RegisterPage
#
# created_user = None
#
#
# def test_register(setup):
#     global created_user
#
#     driver = setup
#     reg = RegisterPage(driver)
#
#     created_user = reg.register_user()
#
#     assert "Welcome" in driver.page_source




# from pages.register_page import RegisterPage
#
#
# def test_register(setup, registered_user):
#     driver = setup
#     reg = RegisterPage(driver)
#
#     reg.register_user(registered_user)
#
#     assert "Welcome" in driver.page_source

def test_register(registered_user):
    assert registered_user is not None