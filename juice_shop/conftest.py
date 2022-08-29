import pytest
from utilities.configs import ReadConfig
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from utilities.driver_factory import DriverFactory


@pytest.fixture
def create_driver():
    driver = DriverFactory.create_driver(driver_id=1)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def open_main_page(create_driver):
    driver = create_driver
    driver.get(ReadConfig.get_main_page_url())
    main_page = MainPage(driver)
    main_page.click_dismiss_button()
    return main_page


@pytest.fixture()
def open_login_page(create_driver):
    driver = create_driver
    driver.get(ReadConfig.get_login_page_url())
    login_page = LoginPage(driver)
    login_page.click_dismiss_button()
    return login_page


@pytest.fixture()
def log_in_with_valid_credentials(create_driver):
    driver = create_driver
    driver.get(ReadConfig.get_login_page_url())
    login_page = LoginPage(driver)
    login_page.click_dismiss_button()
    login_page.fill_email_field(ReadConfig.get_test_email())
    login_page.fill_password_field(ReadConfig.get_test_password())
    login_page.click_login_button()
    main_page = MainPage(driver)
    return main_page
