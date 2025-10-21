import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.TopMenuPage import TopMenuPage
from PageObjects.LoginPage import LoginPage
from PageObjects.RegistrationPage import RegistrationPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegistration:

    def test_successful_registration(self):
        """
        Test the full user registration process with valid data.
        This demonstrates: Form submission, Radio Buttons, Checkboxes.
        """
        print("\nExecuting test: test_successful_registration")
        self.driver.get("https://automationteststore.com/")

        # First, navigate from the home page to the login/register page.
        top_menu = TopMenuPage(self.driver)
        top_menu.go_to_login_page()

        # Now that we are on the correct page, proceed to registration.
        login_page = LoginPage(self.driver)
        login_page.go_to_registration_page()

        registration_page = RegistrationPage(self.driver)

        timestamp = str(int(time.time()))
        user_data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': f'testuser{timestamp}@example.com',
            'address_1': '123 Test Street',
            'city': 'Testville',
            'country': 'United Kingdom',
            'region': 'Greater London',
            'postcode': 'SW1A 0AA',
            'login_name': f'testuser{timestamp}',
            'password': 'Password123!',
            'subscribe': 'no'
        }

        # A print statement to easily find the generated username for the login test.
        print(f"\n---> Generated unique login name: {user_data['login_name']} <---\n")

        registration_page.fill_registration_form(user_data)
        registration_page.click_continue()

        # --- FIX ---
        # The site is now correctly loading the success page.
        # We will wait for the success page URL and verify its header.
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("account/success"), "Did not navigate to the registration success page.")

        success_header = registration_page.get_success_message()
        assert "YOUR ACCOUNT HAS BEEN CREATED!" in success_header.upper(), \
            f"Registration success message not found. Header shown: '{success_header}'"
        print("Successfully registered and verified the success page.")

