import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.HomePage import HomePage
import time


@pytest.mark.usefixtures("setup_and_teardown")
class TestAdvancedFeatures:

    def test_page_navigation(self):
        """
        FIX: The 'Contact Us' link no longer opens a new window.
        This test now verifies correct navigation within the same window.
        """
        print("\nExecuting test: test_page_navigation")
        self.driver.get("https://automationteststore.com/")

        home_page = HomePage(self.driver)
        home_page.click_contact_us()

        # Verify that the URL has changed to the contact page
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("contact"), "Did not navigate to the contact us page.")

        assert "CONTACT US" in self.driver.page_source.upper(), "Contact Us page content not found."
        print("Successfully navigated to and verified the Contact Us page.")

    def test_alert_handling(self):
        """
        Demonstrates handling JavaScript alerts.
        """
        print("\nExecuting test: test_alert_handling")
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        wait = WebDriverWait(self.driver, 10)

        # --- FIX --- The original XPath was too fragile. This CSS selector is more specific.
        js_alert_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='jsAlert()']")))
        js_alert_button.click()

        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Alert text received: '{alert_text}'")
        alert.accept()

        result_text = self.driver.find_element(By.ID, "result").text
        assert "You successfully clicked an alert" in result_text, "Alert was not accepted successfully."
        print("Successfully handled a JS Alert.")

    @pytest.mark.skip(reason="This test is intentionally skipped for demonstration purposes.")
    def test_skipped_example(self):
        """
        This test will be skipped by pytest.
        """
        print("\nThis test should not run.")
        assert False, "This assertion should never be reached."

    @pytest.mark.xfail(reason="This test is expected to fail due to a known bug (ID-123).")
    def test_expected_to_fail_example(self):
        """
        This test is marked as an expected failure (xfail).
        """
        print("\nExecuting a test that is expected to fail.")
        # This simulates a feature that is currently broken
        assert 1 == 2, "This is an expected failure."

    def test_intentional_failure_for_screenshot(self):
        """
        This test will intentionally fail to demonstrate the screenshot-on-failure feature.
        This test is expected to fail. Check the 'Screenshots' folder for the output.
        """
        print("\nExecuting test: test_intentional_failure_for_screenshot")
        self.driver.get("https://automationteststore.com/")
        print("This test will now fail to trigger a screenshot.")
        assert False, "Intentionally failing to test screenshot functionality."

