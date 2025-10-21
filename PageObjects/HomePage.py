from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:
    """
    This class represents the Page Object for the Automation Test Store's Home Page.
    It encapsulates all the locators and actions that can be performed on this page.
    This version includes the ActionChains fix for hover-dependent menus.
    """
    # --- Locators ---
    CURRENCY_BUTTON = (By.XPATH, "(//a[@class='dropdown-toggle'])[1]")
    SEARCH_INPUT = (By.ID, "filter_keyword")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".fa.fa-search")
    SPECIALS_MENU_LINK = (By.XPATH, "//a[@href='https://automationteststore.com/index.php?rt=product/special']")
    MAIN_MENU_LINKS = (By.CSS_SELECTOR, "nav .nav-pills > li > a")

    # --- Locators for Main Menu ---
    APPAREL_AND_ACCESSORIES_MENU = (By.XPATH, "//a[contains(@href, 'path=68')]")
    TSHIRTS_SUBMENU_LINK = (By.XPATH, "(//a[contains(text(), 'T-shirts')])[1]")
    MAKEUP_MENU_LINK = (By.XPATH, "//a[contains(@href, 'path=36')]")
    SKINCARE_MENU_LINK = (By.XPATH, "//a[contains(@href, 'path=43')]")
    FRAGRANCE_MENU_LINK = (By.XPATH, "//a[contains(@href, 'path=49')]")
    MEN_MENU_LINK = (By.XPATH, "//a[contains(@href, 'path=58')]")
    HAIR_CARE_MENU_LINK = (By.XPATH, "//a[contains(@href, 'path=52')]")
    BOOKS_MENU_LINK = (By.XPATH, "//a[contains(@href, 'path=65')]")
    CONTACT_US_LINK = (By.XPATH, "//a[contains(@href, 'contact')]")

    # --- Initializer ---
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # --- Actions ---
    def select_currency(self, currency_name):
        """
        Selects a currency from the dropdown menu.
        This now includes a hover action to ensure the menu is active.
        """
        currency_button = self.wait.until(EC.element_to_be_clickable(self.CURRENCY_BUTTON))
        actions = ActionChains(self.driver)
        actions.move_to_element(currency_button).perform()
        print("Hovered over the currency dropdown button.")
        currency_button.click()
        print("Clicked the currency dropdown button.")

        currency_option_locator = (By.XPATH,
                                   f"//ul[contains(@class, 'currency')]//a[contains(text(), '{currency_name}')]")
        currency_option = self.wait.until(EC.element_to_be_clickable(currency_option_locator))
        currency_option.click()
        print(f"Selected currency: {currency_name}")

    def get_selected_currency_text(self):
        """
        Gets the text of the currently selected currency from the main button.
        """
        currency_button = self.wait.until(EC.visibility_of_element_located(self.CURRENCY_BUTTON))
        return currency_button.text

    def enter_search_keyword(self, keyword):
        """
        Enters a keyword into the search input field.
        """
        self.driver.find_element(*self.SEARCH_INPUT).clear()
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(keyword)
        print(f"Entered '{keyword}' into search bar.")

    def click_search_button(self):
        """
        Clicks the search button.
        """
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        print("Clicked search button.")

    def click_specials_menu(self):
        """
        Clicks on the 'Specials' top menu link.
        """
        self.driver.find_element(*self.SPECIALS_MENU_LINK).click()
        print("Clicked on 'Specials' menu.")

    def get_main_menu_link_texts(self):
        """
        Retrieves the text of all top-level menu items.
        """
        self.wait.until(EC.visibility_of_element_located(self.MAIN_MENU_LINKS))
        menu_elements = self.driver.find_elements(*self.MAIN_MENU_LINKS)
        menu_texts = [element.text.strip() for element in menu_elements if element.text]
        print(f"Found main menu items: {menu_texts}")
        return menu_texts

    def navigate_to_tshirts_via_menu(self):
        """
        Hovers over the 'Apparel & Accessories' menu and clicks on 'T-shirts'.
        """
        apparel_menu = self.wait.until(EC.presence_of_element_located(self.APPAREL_AND_ACCESSORIES_MENU))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", apparel_menu)
        print("Scrolled 'Apparel & Accessories' menu into view.")

        actions = ActionChains(self.driver)
        actions.move_to_element(apparel_menu).perform()
        print("Hovered over 'Apparel & Accessories' menu.")

        tshirts_link = self.wait.until(EC.visibility_of_element_located(self.TSHIRTS_SUBMENU_LINK))

        self.driver.execute_script("arguments[0].click();", tshirts_link)
        print("Clicked on 'T-shirts' sub-menu link using JavaScript.")

    def click_makeup_menu(self):
        """Clicks on the 'Makeup' top menu link."""
        makeup_link = self.wait.until(EC.element_to_be_clickable(self.MAKEUP_MENU_LINK))
        makeup_link.click()
        print("Clicked on 'Makeup' menu.")

    def click_skincare_menu(self):
        """Clicks on the 'Skincare' top menu link."""
        skincare_link = self.wait.until(EC.element_to_be_clickable(self.SKINCARE_MENU_LINK))
        skincare_link.click()
        print("Clicked on 'Skincare' menu.")

    def click_fragrance_menu(self):
        """Clicks on the 'Fragrance' top menu link."""
        fragrance_link = self.wait.until(EC.element_to_be_clickable(self.FRAGRANCE_MENU_LINK))
        fragrance_link.click()
        print("Clicked on 'Fragrance' menu.")

    def click_men_menu(self):
        """Clicks on the 'Men' top menu link."""
        men_link = self.wait.until(EC.element_to_be_clickable(self.MEN_MENU_LINK))
        men_link.click()
        print("Clicked on 'Men' menu.")

    def click_hair_care_menu(self):
        """Clicks on the 'Hair Care' top menu link."""
        hair_care_link = self.wait.until(EC.element_to_be_clickable(self.HAIR_CARE_MENU_LINK))
        hair_care_link.click()
        print("Clicked on 'Hair Care' menu.")

    def click_books_menu(self):
        """Clicks on the 'Books' top menu link."""
        books_link = self.wait.until(EC.element_to_be_clickable(self.BOOKS_MENU_LINK))
        books_link.click()
        print("Clicked on 'Books' menu.")

    def click_contact_us(self):
        """
        FIX: Scrolls to the footer link before clicking to ensure it is visible.
        """
        # First, wait for the element to be present in the DOM
        contact_us_link = self.wait.until(EC.presence_of_element_located(self.CONTACT_US_LINK))

        # Then, scroll the element into view using JavaScript
        self.driver.execute_script("arguments[0].scrollIntoView(true);", contact_us_link)
        print("Scrolled 'Contact Us' link into view.")

        # Finally, wait for the element to be clickable and click it
        self.wait.until(EC.element_to_be_clickable(contact_us_link)).click()
        print("Clicked on 'Contact Us' link.")

