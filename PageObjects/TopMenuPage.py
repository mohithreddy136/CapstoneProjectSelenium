from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TopMenuPage:
    """
    Page Object for the top navigation menu present on most pages.
    """
    # --- Locators ---
    LOGIN_OR_REGISTER_LINK = (By.LINK_TEXT, "Login or register")

    # --- Initializer ---
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # --- Actions ---
    def go_to_login_page(self):
        """Clicks the 'Login or register' link."""
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_OR_REGISTER_LINK)).click()
        print("Clicked 'Login or register' link.")
