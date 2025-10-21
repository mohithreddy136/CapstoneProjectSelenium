from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Page Object for the combined Login / Registration page.
    This version is refactored to handle the login form and its validation messages.
    """
    # --- Locators ---
    # Registration
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[title='Continue']")

    # Login
    LOGIN_NAME_INPUT = (By.ID, "loginFrm_loginname")
    PASSWORD_INPUT = (By.ID, "loginFrm_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[title='Login']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-error.alert-danger")

    # --- Initializer ---
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # --- Actions for Registration ---
    def go_to_registration_page(self):
        """Clicks the 'Continue' button under 'I am a new customer.'"""
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()
        print("Clicked 'Continue' button to proceed to registration page.")

    # --- Actions for Login ---
    def enter_login_name(self, login_name):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_NAME_INPUT)).send_keys(login_name)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_login_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text

