from utilities.wait import wait_until
from utilities.random_generator import generate_random_symbols


def test_check_title(open_main_page):
    """
    @test description: Test verifies that page title is correct
    @test steps:
        1. Open main Page.
        2. Verify page title.
    @expected: main page title >>>
    """
    home_page = open_main_page
    home_page_title = home_page.get_page_title()
    assert home_page_title == 'OWASP Juice Shop', f'Expected: OWASP Juice Shop \n Actual: {home_page_title}'


def test_check_default_item_per_page(open_main_page):
    """
    @test description: Test verifies default elements quantity per pager
    @test steps:
        1. Open main page
        2. Observe "Items per page" drowpdown value
        3. Observe number of Juices on page
    @expected:
        1. "Items per page" drowpdown value is 12
        2. Number of Juices on page is 12
    """
    home_page = open_main_page
    pagination_value = home_page.get_pagination_value()
    assert pagination_value == '12', f"\nActual: {pagination_value}\nExpected: 12"
    products_count = home_page.get_products_quantity()
    assert products_count == int(pagination_value), f"\nActual: {products_count}\nExpected: {pagination_value}"


def test_verify_language_change(open_main_page):
    """
    @test description: test verifies that language can be changed
    @test steps:
        1. open main page
        2. select German language from dropdown
        3. observe items header
    @expected:
        1. items header is "Alle Produkte"
    """
    home_page = open_main_page
    home_page.select_language('Deutsch')
    actual_text = home_page.get_items_header()
    assert actual_text == "Alle Produkte", f"\nActual: {actual_text}\nExpected: 'Alle Produkte'"


def test_verify_searching(open_main_page):
    """
    @test description: test verifies searching
    @test steps:
        1. open main page
        2. get random available product from main page
        3. search for product
        4. search for partial name product
        5. search for incorrect product
    @expected:
        1. search result page contains one product
        2. items header is changed to "Search Results - {search_request}"
    """
    home_page = open_main_page
    product = home_page.choose_random_product()
    home_page.click_search_button()
    home_page.search_request(product)
    expected_result = "Search Results - " + product

    wait_until(lambda: home_page.get_items_header() == expected_result,
               'Product header is not as expected after waiter')
    items_header = home_page.get_items_header()

    assert items_header == expected_result, f"\nActual: {items_header}" \
                                            f"\nExpected: Search Results - {product}"
    assert home_page.get_products_quantity() == 1


def test_no_results_found(open_main_page):
    """
     @test description: test verifies that correct elements are shown if no results found
     @test steps:
         1. open main page
         2. click search button
         3. enter random invalid symbols
         4. press ENTER button
     @expected:
         1. "No results found" title is shown with "Try adjusting your search to find what you're looking for." content
         2. "not found" picture is present
    """
    home_page = open_main_page
    home_page.click_search_button()
    home_page.search_request(generate_random_symbols())
    no_results_title = home_page.get_no_results_found_title()
    no_results_content = home_page.get_no_results_found_content()
    assert no_results_title == "No results found", f"\nActual: {no_results_title}" \
                                                   f"\nExpected: No results found"

    assert no_results_content == "Try adjusting your search to find what you're looking for.", \
        f"\nActual: {no_results_content}" \
        f"\nExpected: Try adjusting your search to find what you're looking for."
    assert home_page.is_not_found_image_present(), "Image is not present!"


def test_open_login_page_from_nav_bar(open_main_page):
    """
     @test description: test verifies that 'Account > Login' button leads to "Login" page
     @test steps:
         1. open main page
         2. click "Account" button
         3. click "Login" button
     @expected:
         1. login page is opened with login form visible
    """
    home_page = open_main_page
    home_page.go_to_login_page()

    assert home_page.is_login_form_present(), "Login form is not present!"
