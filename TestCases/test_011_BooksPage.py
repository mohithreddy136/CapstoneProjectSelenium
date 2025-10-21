import pytest
from PageObjects.HomePage import HomePage
from PageObjects.BooksPage import BooksPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestBooksPage:

    def test_navigate_to_books_page(self):
        """
        Tests navigation to the 'Books' page and verifies the header.
        """
        print("\nExecuting test: test_navigate_to_books_page")
        self.driver.get("https://automationteststore.com/")

        home_page = HomePage(self.driver)
        home_page.click_books_menu()

        books_page = BooksPage(self.driver)
        header_text = books_page.get_header_text()

        assert "BOOKS" in header_text.upper(), "Not on the Books page or header is incorrect."
        print("Successfully navigated to and verified the Books page.")
