from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    """
    Page Object for the user registration form.
    """
    # --- Locators ---
    FIRST_NAME_INPUT = (By.ID, "AccountFrm_firstname")
    LAST_NAME_INPUT = (By.ID, "AccountFrm_lastname")
    EMAIL_INPUT = (By.ID, "AccountFrm_email")
    ADDRESS_1_INPUT = (By.ID, "AccountFrm_address_1")
    CITY_INPUT = (By.ID, "AccountFrm_city")
    REGION_DROPDOWN = (By.ID, "AccountFrm_zone_id")
    POSTCODE_INPUT = (By.ID, "AccountFrm_postcode")
    COUNTRY_DROPDOWN = (By.ID, "AccountFrm_country_id")
    LOGIN_NAME_INPUT = (By.ID, "AccountFrm_loginname")
    PASSWORD_INPUT = (By.ID, "AccountFrm_password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "AccountFrm_confirm")
    SUBSCRIBE_RADIO_YES = (By.ID, "AccountFrm_newsletter1")
    SUBSCRIBE_RADIO_NO = (By.ID, "AccountFrm_newsletter0")
    PRIVACY_POLICY_CHECKBOX = (By.ID, "AccountFrm_agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[title='Continue']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".maintext")

    # --- Initializer ---
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # --- Actions ---
    def fill_registration_form(self, user_data):
        """
        Fills the entire registration form with data from a dictionary.
        """
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT)).send_keys(user_data['first_name'])
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(user_data['last_name'])
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(user_data['email'])
        self.driver.find_element(*self.ADDRESS_1_INPUT).send_keys(user_data['address_1'])
        self.driver.find_element(*self.CITY_INPUT).send_keys(user_data['city'])

        Select(self.driver.find_element(*self.COUNTRY_DROPDOWN)).select_by_visible_text(user_data['country'])
        print(f"Selected country: {user_data['country']}")

        region_option_locator = (By.XPATH, f"//select[@id='AccountFrm_zone_id']/option[text()='{user_data['region']}']")
        self.wait.until(EC.element_to_be_clickable(region_option_locator))
        print(f"Region '{user_data['region']}' is now available.")

        Select(self.driver.find_element(*self.REGION_DROPDOWN)).select_by_visible_text(user_data['region'])
        print(f"Selected region: {user_data['region']}")

        self.driver.find_element(*self.POSTCODE_INPUT).send_keys(user_data['postcode'])
        self.driver.find_element(*self.LOGIN_NAME_INPUT).send_keys(user_data['login_name'])
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(user_data['password'])
        self.driver.find_element(*self.CONFIRM_PASSWORD_INPUT).send_keys(user_data['password'])

        if user_data['subscribe'].lower() == 'yes':
            self.driver.find_element(*self.SUBSCRIBE_RADIO_YES).click()
        else:
            self.driver.find_element(*self.SUBSCRIBE_RADIO_NO).click()

        # --- FIX --- Using JavaScript to click the checkbox to avoid interception errors.
        privacy_checkbox = self.wait.until(EC.presence_of_element_located(self.PRIVACY_POLICY_CHECKBOX))
        self.driver.execute_script("arguments[0].click();", privacy_checkbox)
        print("Clicked the privacy policy checkbox using JavaScript.")
        print("Filled out the registration form.")

    def click_continue(self):
        """Clicks the final continue button using JavaScript to ensure the form submits."""
        # --- FIX --- Using JavaScript to click the button for maximum reliability.
        continue_button = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        self.driver.execute_script("arguments[0].click();", continue_button)
        print("Clicked the final 'Continue' button using JavaScript.")

    def get_success_message(self):
        """Gets the success message text after registration."""
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).text

