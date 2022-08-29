from contextlib import suppress
import allure
import pytest
from utilities.configs import ReadConfig
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from utilities.driver_factory import DriverFactory


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def create_driver(request):
    driver = DriverFactory.create_driver(driver_id=1)
    driver.maximize_window()
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
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
