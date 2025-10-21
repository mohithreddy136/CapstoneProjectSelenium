from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ApparelPage:
    """
    Page Object for the 'Apparel & Accessories' category pages.
    """
    # --- Locators ---
    PAGE_HEADER = (By.CSS_SELECTOR, ".maintext")
    BREADCRUMB_TRAIL = (By.CSS_SELECTOR, ".breadcrumb")

    # --- Initializer ---
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # --- Actions ---
    def get_header_text(self):
        """Gets the main header text of the page."""
        return self.wait.until(EC.visibility_of_element_located(self.PAGE_HEADER)).text

    def get_breadcrumb_text(self):
        """Gets the text of the breadcrumb navigation trail."""
        return self.wait.until(EC.visibility_of_element_located(self.BREADCRUMB_TRAIL)).text
