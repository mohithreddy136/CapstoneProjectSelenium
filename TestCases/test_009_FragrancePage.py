import pytest
from PageObjects.HomePage import HomePage
from PageObjects.FragrancePage import FragrancePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestFragrancePage:

    def test_navigate_to_fragrance_and_verify_header(self):
        """
        Tests navigation to the Fragrance page and verifies its header.
        """
        print("\nExecuting test: test_navigate_to_fragrance_and_verify_header")
        self.driver.get("https://automationteststore.com/")

        home_page = HomePage(self.driver)
        home_page.click_fragrance_menu()

        fragrance_page = FragrancePage(self.driver)
        header_text = fragrance_page.get_header_text()

        assert "FRAGRANCE" in header_text.upper(), f"Header mismatch. Expected 'FRAGRANCE', but got '{header_text}'."
        print("Successfully navigated to the Fragrance page and verified the header.")

    def test_verify_fragrance_products_are_listed(self):
        """
        Tests that the Fragrance page lists at least one product.
        """
        print("\nExecuting test: test_verify_fragrance_products_are_listed")
        self.driver.get("https://automationteststore.com/")

        home_page = HomePage(self.driver)
        home_page.click_fragrance_menu()

        fragrance_page = FragrancePage(self.driver)
        product_list = fragrance_page.get_product_names()

        assert len(product_list) > 0, "No products were found on the Fragrance page."
        print(f"Verified that {len(product_list)} products are listed on the page.")
