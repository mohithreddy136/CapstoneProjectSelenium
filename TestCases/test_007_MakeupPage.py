import pytest
from PageObjects.HomePage import HomePage
from PageObjects.MakeupPage import MakeupPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestMakeupPage:

    def test_navigate_to_makeup_page_and_verify_header(self):
        """
        Tests navigation to the makeup page and verifies its header.
        """
        print("\nExecuting test: test_navigate_to_makeup_page_and_verify_header")
        self.driver.get("https://automationteststore.com/")

        home_page = HomePage(self.driver)
        home_page.click_makeup_menu()

        makeup_page = MakeupPage(self.driver)
        header_text = makeup_page.get_header_text()

        assert "MAKEUP" in header_text.upper(), f"Header mismatch. Expected 'MAKEUP', but got '{header_text}'."
        print("Successfully navigated to the Makeup page and verified the header.")

    def test_verify_products_are_listed(self):
        """
        Tests that the makeup page lists at least one product.
        """
        print("\nExecuting test: test_verify_products_are_listed")
        self.driver.get("https://automationteststore.com/")

        home_page = HomePage(self.driver)
        home_page.click_makeup_menu()

        makeup_page = MakeupPage(self.driver)
        product_list = makeup_page.get_product_names()

        assert len(product_list) > 0, "No products were found on the Makeup page."
        print(f"Verified that {len(product_list)} products are listed on the page.")
