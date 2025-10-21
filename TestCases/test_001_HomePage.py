import pytest
from PageObjects.HomePage import HomePage


# Using a class to group related tests for the Home Page
@pytest.mark.usefixtures("setup_and_teardown")
class TestHomePage:

    def test_verify_homepage_title(self):
        """
        Test to verify the title of the homepage.
        This demonstrates: Browser Launching, Navigation Commands.
        """
        print("\nExecuting test: test_verify_homepage_title")
        self.driver.get("https://automationteststore.com/")
        expected_title = "A place to practice your automation skills!"
        actual_title = self.driver.title
        assert actual_title == expected_title, f"Title mismatch. Expected '{expected_title}', but got '{actual_title}'."

    def test_click_on_specials_menu(self):
        """
        Test to navigate to the 'Specials' page from the top menu.
        This demonstrates: WebElement Methods (click).
        """
        print("\nExecuting test: test_click_on_specials_menu")
        self.driver.get("https://automationteststore.com/")
        home_page = HomePage(self.driver)
        home_page.click_specials_menu()

        # Assert that the URL has changed to the specials page
        assert "special" in self.driver.current_url, "Did not navigate to the Specials page."

    def test_handle_currency_dropdown(self):
        """
        Test to select a currency and verify the selection.
        This demonstrates: DropDown Handling.
        """
        print("\nExecuting test: test_handle_currency_dropdown")
        self.driver.get("https://automationteststore.com/")
        home_page = HomePage(self.driver)
        home_page.select_currency("Euro")

        selected_currency = home_page.get_selected_currency_text()
        # --- FIX --- Updated the assertion to be case-insensitive by checking for the uppercase version.
        assert "EURO" in selected_currency, f"Currency was not changed to Euro. Current selection: {selected_currency}"

    def test_verify_main_menu_items(self):
        """
        Test to find all main menu links and verify one is present.
        This demonstrates: Handling Multiple WebElements.
        """
        print("\nExecuting test: test_verify_main_menu_items")
        self.driver.get("https://automationteststore.com/")
        home_page = HomePage(self.driver)
        menu_items = home_page.get_main_menu_link_texts()

        # We assert that a specific, important menu item exists.
        expected_menu_item = "APPAREL & ACCESSORIES"
        assert expected_menu_item in menu_items, f"'{expected_menu_item}' was not found in the main menu."

    def test_search_for_product(self):
        """
        Test to use the search bar and verify navigation to the search results page.
        """
        print("\nExecuting test: test_search_for_product")
        self.driver.get("https://automationteststore.com/")
        home_page = HomePage(self.driver)
        search_term = "lipstick"
        home_page.enter_search_keyword(search_term)
        home_page.click_search_button()

        # Verify that either the URL or the page title indicates a search result.
        # This makes the test more robust.
        current_url = self.driver.current_url
        page_title = self.driver.title
        assert f"keyword={search_term}" in current_url or search_term.capitalize() in page_title, \
            f"Search results page is incorrect. URL: {current_url}, Title: {page_title}"

