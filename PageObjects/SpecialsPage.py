from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SpecialsPage:
    """
    Page Object for the 'Specials' page, which lists products on sale.
    """
    # --- Locators ---
    PAGE_HEADER = (By.CSS_SELECTOR, ".maintext")
    PRODUCT_THUMBNAILS = (By.CSS_SELECTOR, ".thumbnail")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".fixed .prdocutname") # Note the typo 'prdocutname' is correct in the site's HTML
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".productcart")

    # --- Initializer ---
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # --- Actions ---
    def get_header_text(self):
        """Gets the main header text of the page."""
        return self.wait.until(EC.visibility_of_element_located(self.PAGE_HEADER)).text

    def get_all_product_names(self):
        """Returns a list of all product names visible on the page."""
        product_elements = self.wait.until(EC.visibility_of_all_elements_located(self.PRODUCT_NAMES))
        return [elem.text for elem in product_elements]

    def add_first_product_to_cart(self):
        """Finds the first product on the page and clicks its 'Add to Cart' button."""
        first_product_container = self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_THUMBNAILS)
        )
        add_to_cart_button = first_product_container.find_element(*self.ADD_TO_CART_BUTTONS)
        add_to_cart_button.click()
        print("Clicked 'Add to Cart' for the first special product.")
