import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.HomePage import HomePage
from PageObjects.SpecialsPage import SpecialsPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSpecialsPage:

    def test_navigate_and_verify_specials_page(self):
        """
        Tests navigation to the 'Specials' page and verifies its content.
        """
        print("\nExecuting test: test_navigate_and_verify_specials_page")
        self.driver.get("https://automationteststore.com/")

        home_page = HomePage(self.driver)
        home_page.click_specials_menu()

        specials_page = SpecialsPage(self.driver)

        # 1. Verify the header
        header_text = specials_page.get_header_text()
        # --- FIX --- The header text changed from "SPECIALS" to "SPECIAL OFFERS".
        assert "SPECIAL OFFERS" in header_text.upper(), "Not on the Specials page."
        print(f"Successfully navigated to Specials page with header: '{header_text}'")

        # 2. Verify that products are listed
        product_names = specials_page.get_all_product_names()
        assert len(product_names) > 0, "No products found on the Specials page."
        print(f"Found {len(product_names)} products on the page.")

    def test_add_special_product_to_cart(self):
        """
        Tests adding a product from the 'Specials' page to the shopping cart.
        """
        print("\nExecuting test: test_add_special_product_to_cart")
        self.driver.get("https://automationteststore.com/")

        home_page = HomePage(self.driver)
        home_page.click_specials_menu()

        specials_page = SpecialsPage(self.driver)

        # Get the name of the first product to verify it later in the cart
        first_product_name = specials_page.get_all_product_names()[0]
        print(f"Attempting to add '{first_product_name}' to the cart.")

        specials_page.add_first_product_to_cart()

        # Verify the product is in the cart
        self.driver.get("https://automationteststore.com/index.php?rt=checkout/cart")
        wait = WebDriverWait(self.driver, 10)
        # --- FIX --- The original CSS selector for the cart was incorrect. This is more robust.
        cart_product_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td.align_left a"))).text

        # --- FIX --- Making the assertion case-insensitive to handle capitalization differences.
        assert first_product_name.upper() in cart_product_name.upper(), f"Product '{first_product_name}' not found in cart."
        print(f"Verified '{cart_product_name}' is in the shopping cart.")

