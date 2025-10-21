import pytest
from PageObjects.TopMenuPage import TopMenuPage
from PageObjects.LoginPage import LoginPage
from Utilities.ExcelReader import get_data_from_excel


@pytest.mark.usefixtures("setup_and_teardown")
class TestLoginDDT:
    # Define the path to the test data
    file_path = "TestData/LoginData.xlsx"
    sheet_name = "Login"

    @pytest.mark.parametrize("username, password, expected_result", get_data_from_excel(file_path, sheet_name))
    @pytest.mark.regression
    def test_login_with_data(self, username, password, expected_result):
        """
        Tests the login functionality with data from an Excel file.
        This demonstrates: Data-Driven Testing, Parameterization, Markers.
        """
        print(f"\nExecuting test: test_login_with_data for user: {username}")
        self.driver.get("https://automationteststore.com/")

        top_menu = TopMenuPage(self.driver)
        top_menu.go_to_login_page()

        login_page = LoginPage(self.driver)
        login_page.enter_login_name(username)
        login_page.enter_password(password)
        login_page.click_login_button()

        if expected_result.lower() == 'success':
            # For a successful login, we should land on the account page
            assert "MY ACCOUNT" in self.driver.page_source.upper(), "Login failed for a valid user."
            print(f"Login successful for user: {username}")
        else:
            # For a failed login, we should see an error message
            error_message = login_page.get_login_error_message()
            assert "ERROR: INCORRECT LOGIN OR PASSWORD PROVIDED." in error_message.upper(), \
                "Error message not displayed for an invalid login."
            print(f"Login correctly failed for user: {username}")
