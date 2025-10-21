from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MakeupPage:
    """
    Page Object for the Makeup category page.
    """
    # --- Locators ---
    PAGE_HEADER = (By.CSS_SELECTOR, "h1 .maintext")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".fixed_wrapper .prdocutname")

    # --- Initializer ---
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # --- Actions ---
    def get_header_text(self):
        """Gets the text of the main page header."""
        header = self.wait.until(EC.visibility_of_element_located(self.PAGE_HEADER))
        return header.text

    def get_product_names(self):
        """Returns a list of all product name elements on the page."""
        products = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_NAMES))
        return products
