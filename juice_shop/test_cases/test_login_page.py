from utilities.wait import wait_until
from utilities.random_generator import generate_random_symbols
from utilities.configs import ReadConfig


def test_login_form_is_complete(open_login_page):
    """
     @test description: test verifies that Login form contains all required elements
     @test preconditions: login screen is opened
     @test steps:
         1. observe login form header
         2. observe Email field
         3. observe Password field
         4. observe 'button to show password'
         5. observe 'Forgot password' button
         6. observe 'Log in' button
         7. observe 'Remember me' checkbox
         8. observe 'Log in with Google' button
         9. observe 'Not yet a customer' button
     @expected:
         1. login form header is 'Login'
         2. Email field is present
         3. Password field is present
         4. 'button to show password' is present
         5. 'Forgot password' button is present
         6. 'Log in' button is present
         7. 'Remember me' checkbox is present
         8. 'Log in with Google' button is present
         9. 'Not yet a customer' button is present
    """
    login_page = open_login_page
    login_header = login_page.get_login_header()

    assert login_header == "Login", f"\nActual: {login_header}\nExpected: Login"
    assert login_page.is_email_field_present(), "Email field is not present!"
    assert login_page.is_password_field_present(), "Password field is not present!"
    assert login_page.is_button_to_show_password_present(), "Button to show password is not present!"
    assert login_page.is_forgot_password_button_present(), "Forgot password button is not present!"
    assert login_page.is_login_button_present(), "Login button is not present!"
    assert login_page.is_remember_me_checkbox_present(), "Remember me checkbox is not present!"
    assert login_page.is_login_with_google_button_present(), "Login with Google button is not present!"
    assert login_page.is_not_yet_a_customer_button_present(), "Not yet a customer button is not present!"


def test_login_button_disabled_by_default(open_login_page):
    """
     @test description: test verifies that 'Log in' button is disabled by default
     @test steps:
         1. open Login page
         2. observe 'Log in' button
     @expected:
         'Log in' button is disabled by default
    """
    login_page = open_login_page
    login_button_disabled_attr = login_page.get_element_attribute(login_page.is_login_button_present(), 'disabled')

    assert login_button_disabled_attr == "true"


def test_email_validation_error(open_login_page):
    """
     @test description: test verifies that Email validation error is displayed while
                        switching focus from empty Email field.
     @test steps:
         1. open Login page
         2. click on 'Email' field
         3. click outside 'Email' field
     @expected:
         "Please provide an email address." validation error is shown.
    """
    login_page = open_login_page
    login_page.is_email_field_present().click()
    login_page.is_login_button_present().click()
    expected_result = "Please provide an email address."
    wait_until(lambda: login_page.get_email_validation_error_message() == expected_result,
               'Email validation error message is not as expected after waiter')
    error_message = login_page.get_email_validation_error_message()

    assert error_message == expected_result, f"\nActual: {error_message}\nExpected: {expected_result}"


def test_password_validation_error(open_login_page):
    """
     @test description: test verifies that Password validation error is displayed while
                        switching focus from empty Password field.
     @test steps:
         1. open Login page
         2. click on 'Password' field
         3. click outside 'Password' field
     @expected:
         "Please provide a password." validation error is shown.
    """
    login_page = open_login_page
    login_page.is_password_field_present().click()
    login_page.is_login_header_present().click()
    expected_result = "Please provide a password."
    wait_until(lambda: login_page.get_password_validation_error_message() == expected_result,
               'Password validation error message is not as expected after waiter')
    error_message = login_page.get_password_validation_error_message()

    assert error_message == expected_result, f"\nActual: {error_message}\nExpected: {expected_result}"


def test_login_with_invalid_credentials(open_login_page):
    login_page = open_login_page
    login_page.fill_email_field(generate_random_symbols())
    login_page.fill_password_field(generate_random_symbols())
    login_page.click_login_button()

    error_message = login_page.get_invalid_credentials_error_message()

    assert error_message == "Invalid email or password.", f"\nActual: {error_message}" \
                                                          f"\nExpected: Invalid email or password."


def test_login_with_valid_credentials(log_in_with_valid_credentials):
    main_page = log_in_with_valid_credentials
    main_page.click_account_button()
    actual_email = main_page.get_email_of_logged_in_user()

    assert actual_email == ReadConfig.get_test_email(), f"\nActual: {actual_email}" \
                                                        f"\nExpected: {ReadConfig.get_test_email()}"
