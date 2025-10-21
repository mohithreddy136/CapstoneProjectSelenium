import pytest
from PageObjects.HomePage import HomePage
from PageObjects.ApparelPage import ApparelPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestApparelPage:

    def test_navigate_to_tshirts_subcategory(self):
        """
        Tests navigation to the T-shirts sub-category via the hover menu.
        This demonstrates: Mouse Hover Actions (ActionChains).
        """
        print("\nExecuting test: test_navigate_to_tshirts_subcategory")
        self.driver.get("https://automationteststore.com/")

        home_page = HomePage(self.driver)
        home_page.navigate_to_tshirts_via_menu()

        apparel_page = ApparelPage(self.driver)

        # Verify landing on the T-shirts page by checking the breadcrumb
        breadcrumb_text = apparel_page.get_breadcrumb_text()
        assert "APPAREL & ACCESSORIES" in breadcrumb_text.upper()
        assert "T-SHIRTS" in breadcrumb_text.upper(), "Did not navigate to the T-shirts sub-category."
        print(f"Successfully navigated to T-shirts page. Breadcrumb: '{breadcrumb_text}'")
