from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FragrancePage:
    """
    Page Object for the Fragrance category page.
    """
    # --- Locators ---
    PAGE_HEADER = (By.CSS_SELECTOR, "h1 .maintext")
    PRODUCT_GRID = (By.CSS_SELECTOR, ".thumbnails.grid.row")
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
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_GRID))
        products = self.driver.find_elements(*self.PRODUCT_NAMES)
        return products
