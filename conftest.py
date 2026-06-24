import pytest
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.register_page import RegisterPage


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def registered_user():
    username = "sai" + str(random.randint(1000, 9999))

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    reg = RegisterPage(driver)
    reg.register_user(username)

    driver.quit()

    return username