import pytest
from PageObjects.TopMenuPage import TopMenuPage
from PageObjects.LoginPage import LoginPage
from Utilities.ExcelReader import get_data_from_excel


@pytest.mark.usefixtures("setup_and_teardown")
class TestLoginDDT:
    # Define the path to the test data
    file_path = "TestData/LoginData.xlsx"
    sheet_name = "Login"

    # --- MODIFIED --- Pass row_limit=1 to only read the first data row
    test_data = get_data_from_excel(file_path, sheet_name, row_limit=1)

    # --- MODIFIED --- Use the pre-fetched test_data variable
    @pytest.mark.parametrize("username, password, expected_result", test_data)
    @pytest.mark.regression
    def test_login_with_data(self, username, password, expected_result):
        """
        Tests the login functionality with data from an Excel file.
        This demonstrates: Data-Driven Testing, Parameterization, Markers.
        Now limited to the first data row.
        """
        print(f"\nExecuting test: test_login_with_data for user: {username}")
        # --- Basic Check --- Add a check to ensure data was loaded
        if not username:
            pytest.skip("Skipping test, no username provided in test data.")

        self.driver.get("https://automationteststore.com/")

        top_menu = TopMenuPage(self.driver)
        top_menu.go_to_login_page()

        login_page = LoginPage(self.driver)
        login_page.enter_login_name(username)
        login_page.enter_password(password)
        login_page.click_login_button()

        if expected_result.lower() == 'success':
            # For a successful login, we should land on the account page
            # --- Robust Check --- Wait for a specific element on the account page
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.common.by import By
            wait = WebDriverWait(self.driver, 10)
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(., 'My Account')]")),
                           "Did not land on 'My Account' page after successful login.")
                print(f"Login successful for user: {username}")
            except Exception as e:
                pytest.fail(f"Login failed for a valid user '{username}'. Exception: {e}")

        else:
            # For a failed login, we should see an error message
            error_message = login_page.get_login_error_message()
            assert "ERROR: INCORRECT LOGIN OR PASSWORD PROVIDED." in error_message.upper(), \
                "Error message not displayed or incorrect for an invalid login."
            print(f"Login correctly failed for user: {username}")
