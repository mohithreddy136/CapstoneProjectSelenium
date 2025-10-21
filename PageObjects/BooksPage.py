from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BooksPage:
    """
    Page Object for the Books category page.
    """
    # --- Locators ---
    PAGE_HEADER = (By.CSS_SELECTOR, ".maintext")

    # --- Initializer ---
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # --- Actions ---
    def get_header_text(self):
        """
        Gets the text of the main page header.
        """
        header = self.wait.until(EC.visibility_of_element_located(self.PAGE_HEADER))
        return header.text
