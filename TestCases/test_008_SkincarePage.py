import pytest
from PageObjects.HomePage import HomePage
from PageObjects.SkincarePage import SkincarePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSkincarePage:

    def test_navigate_to_skincare_and_verify_header(self):
        """
        Tests navigation to the Skincare page and verifies its header.
        """
        print("\nExecuting test: test_navigate_to_skincare_and_verify_header")
        self.driver.get("https://automationteststore.com/")

        home_page = HomePage(self.driver)
        home_page.click_skincare_menu()

        skincare_page = SkincarePage(self.driver)
        header_text = skincare_page.get_header_text()

        assert "SKINCARE" in header_text.upper(), f"Header mismatch. Expected 'SKINCARE', but got '{header_text}'."
        print("Successfully navigated to the Skincare page and verified the header.")

    def test_verify_skincare_products_are_listed(self):
        """
        Tests that the Skincare page lists at least one product.
        """
        print("\nExecuting test: test_verify_skincare_products_are_listed")
        self.driver.get("https://automationteststore.com/")

        home_page = HomePage(self.driver)
        home_page.click_skincare_menu()

        skincare_page = SkincarePage(self.driver)
        product_list = skincare_page.get_product_names()

        assert len(product_list) > 0, "No products were found on the Skincare page."
        print(f"Verified that {len(product_list)} products are listed on the page.")
