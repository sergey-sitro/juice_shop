from utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    __login_header = (By.XPATH, "//mat-card/h1")
    __email_field = (By.XPATH, "//input[@name='email']")
    __password_field = (By.XPATH, "//input[@name='password']")
    __button_to_hide_password = (By.XPATH, "//button[@aria-label='Button to hide the password']")
    __button_to_show_password = (By.XPATH, "//button[@aria-label='Button to display the password']")
    __forgot_password_button = (By.XPATH, "//a[@routerlink='/forgot-password']")
    __login_button = (By.XPATH, "//button[@id='loginButton']")
    __remember_me_checkbox = (By.XPATH, "//mat-checkbox[@id='rememberMe']")
    __login_with_google_button = (By.XPATH, "//button[@id='loginButtonGoogle']")
    __not_yet_a_customer_button = (By.XPATH, "//a[@routerlink='/register']")
    __email_validation_error = (By.XPATH, "//mat-error[@id='mat-error-0']")
    __password_validation_error = (By.XPATH, "//mat-error[@id='mat-error-1']")
    __invalid_credentials_error = (By.XPATH, "//div[@class='error ng-star-inserted']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_header(self):
        return self.get_text(self.__login_header)

    def is_login_header_present(self):
        return self.wait_for_element_located(self.__login_header)

    def is_email_field_present(self):
        return self.wait_for_element_located(self.__email_field)

    def is_password_field_present(self):
        return self.wait_for_element_located(self.__password_field)

    def is_button_to_show_password_present(self):
        return self.wait_for_element_located(self.__button_to_show_password)

    def is_button_to_hide_password_present(self):
        return self.wait_for_element_located(self.__button_to_hide_password)

    def is_forgot_password_button_present(self):
        return self.wait_for_element_located(self.__forgot_password_button)

    def is_login_button_present(self):
        return self.wait_for_element_located(self.__login_button)

    def is_remember_me_checkbox_present(self):
        return self.wait_for_element_located(self.__remember_me_checkbox)

    def is_login_with_google_button_present(self):
        return self.wait_for_element_located(self.__login_with_google_button)

    def is_not_yet_a_customer_button_present(self):
        return self.wait_for_element_located(self.__not_yet_a_customer_button)

    def get_email_validation_error_message(self):
        return self.get_text(self.__email_validation_error)

    def get_password_validation_error_message(self):
        return self.get_text(self.__password_validation_error)

    def fill_email_field(self, content):
        email_field = self.wait_for_element_located(self.__email_field)
        email_field.send_keys(content)

    def fill_password_field(self, content):
        email_field = self.wait_for_element_located(self.__password_field)
        email_field.send_keys(content)

    def click_login_button(self):
        self.click(self.__login_button)

    def is_invalid_credentials_error_present(self):
        return self.wait_for_element_located(self.__invalid_credentials_error)

    def get_invalid_credentials_error_message(self):
        return self.get_text(self.__invalid_credentials_error)
