import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage
import allure
from allure_commons.types import AttachmentType


class MainPage(BasePage):
    __page_title = (By.XPATH, '//button[@aria-label= "Back to homepage"]/span[@class="mat-button-wrapper"]/span')
    __pagination_dropdown = (By.XPATH, "//mat-select[@role='combobox']")
    __product = (By.CSS_SELECTOR, "mat-card")
    __product_name = (By.CSS_SELECTOR, "[class='item-name']")
    __language_button = (By.XPATH, "//button[@aria-label='Language selection menu']")
    __language_radio_button = (By.XPATH, "//span[@class='mat-radio-label-content']/div")
    __items_header = (By.XPATH, "//app-search-result/div/div/div/div[@class='ng-star-inserted']")
    __search_button = (By.XPATH, "//mat-icon[normalize-space(text()) = 'search']")
    __search_input = (By.XPATH, "//input")
    __no_results_found_title = (By.XPATH, "//mat-card-title/span[@class='noResultText']")
    __no_results_found_content = (By.XPATH, "//mat-card-content/span[@class='noResultText']")
    __no_results_found_image = (By.XPATH, "//img[@class='img-responsive noResult']")
    __account_button = (By.XPATH, "//button[@id='navbarAccount']")
    __account_login_button = (By.XPATH, "//button[@id='navbarLoginButton']")
    __login_form = (By.XPATH, "//mat-card")
    __logged_in_user_email = (By.XPATH, "//button[@aria-label='Go to user profile']/span")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.get_text(self.__page_title)

    def get_pagination_value(self):
        return self.get_text(self.__pagination_dropdown)

    def get_products_quantity(self):
        return len(self.wait_for_elements_located(self.__product))

    def select_language(self, language):
        self.click(self.__language_button)
        self.select_from_menu_content(language, self.__language_radio_button)

    def get_items_header(self):
        return self.get_text(self.__items_header)

    def choose_random_product(self):
        products = self.wait_for_elements_located(self.__product_name)
        random_product = random.choice(products)
        return random_product.text

    def click_search_button(self):
        self.click(self.__search_button)

    def search_request(self, request):
        search_field = self.wait_for_element_located(self.__search_input)
        search_field.send_keys(request)
        search_field.send_keys(Keys.RETURN)

    def get_no_results_found_title(self):
        return self.get_text(self.__no_results_found_title)

    def get_no_results_found_content(self):
        return self.get_text(self.__no_results_found_content)

    def is_not_found_image_present(self):
        return self.wait_for_element_located(self.__no_results_found_image)

    def go_to_login_page(self):
        account_button = self.wait_for_element_located(self.__account_button)
        account_button.click()
        account_login_button = self.wait_for_element_located(self.__account_login_button)
        account_login_button.click()

    def is_login_form_present(self):
        return self.wait_for_element_located(self.__login_form)

    def click_account_button(self):
        self.click(self.__account_button)

    def get_email_of_logged_in_user(self):
        return self.get_text(self.__logged_in_user_email)
