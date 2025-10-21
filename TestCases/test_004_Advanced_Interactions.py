import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import urllib3

# Suppress the InsecureRequestWarning for unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@pytest.mark.usefixtures("setup_and_teardown")
class TestAdvancedInteractions:

    @pytest.mark.smoke
    def test_drag_and_drop(self):
        """
        Demonstrates Drag and Drop, Right Click, and Alert Handling.
        """
        print("\nExecuting test: test_drag_and_drop_and_right_click")
        self.driver.get("https://jqueryui.com/droppable/")
        wait = WebDriverWait(self.driver, 10)

        # --- Frame Handling ---
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, ".demo-frame")))
        print("Switched to the iframe.")

        # --- Drag and Drop ---
        source_element = wait.until(EC.visibility_of_element_located((By.ID, "draggable")))
        target_element = wait.until(EC.visibility_of_element_located((By.ID, "droppable")))
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()
        print("Drag and drop action performed.")
        assert "Dropped!" in target_element.text, "Drag and drop failed."

        # --- Right Click (Context Click) ---
        actions.context_click(target_element).perform()
        print("Right-click action performed on the target element.")
        self.driver.switch_to.default_content()

    # def test_web_table_and_scrolling(self):
    #     """
    #     Demonstrates handling a web table and scrolling the page.
    #     """
    #     print("\nExecuting test: test_web_table_and_scrolling")
    #     self.driver.get("https://automationteststore.com/")
    #     wait = WebDriverWait(self.driver, 10)
    #
    #     # --- FIX: Changed wait condition to handle elements that are not immediately visible ---
    #     # 1. Wait for the tab link to be PRESENT in the DOM, even if it's off-screen.
    #     featured_tab_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='#featured']")))
    #
    #     # 2. Now that we have the element, scroll to it.
    #     self.driver.execute_script("arguments[0].scrollIntoView();", featured_tab_link)
    #     print("Scrolled down to the product tabs.")
    #
    #     # 3. Wait for the tab to be CLICKABLE before clicking.
    #     wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='#featured']"))).click()
    #     print("Clicked the 'Featured' tab to ensure its content is active.")
    #
    #     # 4. Now, wait for the product content within the active tab to be visible.
    #     product_names_selector = "#featured .productname"
    #     product_prices_selector = "#featured .pricenew"
    #
    #     wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, product_names_selector)))
    #     print("Product elements are now visible on the page.")
    #
    #     product_names = self.driver.find_elements(By.CSS_SELECTOR, product_names_selector)
    #     product_prices = self.driver.find_elements(By.CSS_SELECTOR, product_prices_selector)
    #
    #     assert len(product_names) > 0, "No products found in the featured table."
    #     print("\n--- Featured Products ---")
    #     for i in range(len(product_names)):
    #         print(f"Product: {product_names[i].text}, Price: {product_prices[i].text}")
    #     print("------------------------")
    #
    #     # --- Scroll Up ---
    #     self.driver.execute_script("window.scrollTo(0, 0);")
    #     print("Scrolled back to the top of the page.")

    def test_add_featured_product_to_cart(self):
        """
        Tests adding a specific featured product ("Benefit Bella Bamba") to the cart
        and verifies the product name before adding.
        """
        print("\nExecuting test: test_add_featured_product_to_cart")
        self.driver.get("https://automationteststore.com/")
        wait = WebDriverWait(self.driver, 10)

        # --- FIX: Changed wait condition to handle elements that are not immediately visible ---
        # 1. Wait for the tab link to be PRESENT in the DOM, then scroll to it.
        featured_tab_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='#featured']")))
        self.driver.execute_script("arguments[0].scrollIntoView();", featured_tab_link)

        # 2. Wait for the tab to be CLICKABLE before clicking.
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='#featured']"))).click()
        print("Clicked the 'Featured' tab.")

        # 3. Find the specific product container.
        product_container_xpath = "//div[@id='featured']//div[contains(@class, 'thumbnail') and .//a[contains(@href, 'id=52')]]"
        product_container = wait.until(EC.visibility_of_element_located((By.XPATH, product_container_xpath)))

        # 4. Verify the product name text within the container.
        product_name_element = product_container.find_element(By.CSS_SELECTOR, ".productname")
        assert "Benefit Bella Bamba" in product_name_element.text, "The product name is incorrect."
        print(f"Verified product name: '{product_name_element.text}'")

        # 5. Locate and click the 'Add to Cart' button within the same container.
        add_to_cart_button = product_container.find_element(By.CSS_SELECTOR, "a.cart")
        add_to_cart_button.click()
        print("Clicked 'Add to Cart' for Benefit Bella Bamba.")

        # 6. Navigate to the shopping cart page to verify.
        self.driver.get("https://automationteststore.com/index.php?rt=checkout/cart")

        # 7. Assert that the product name is present in the cart's page source.
        page_source = self.driver.page_source
        assert "Benefit Bella Bamba" in page_source, "Product was not found in the shopping cart."
        print("Verified that 'Benefit Bella Bamba' is in the shopping cart.")

    # @pytest.mark.regression
    # def test_broken_links(self):
    #     """
    #     Finds all links on the page and checks their HTTP status.
    #     This demonstrates: Broken Link Checking.
    #     """
    #     print("\nExecuting test: test_broken_links")
    #     self.driver.get("https://automationteststore.com/")
    #
    #     all_links = self.driver.find_elements(By.TAG_NAME, "a")
    #     urls = [link.get_attribute("href") for link in all_links if link.get_attribute("href")]
    #
    #     print(f"Found {len(urls)} URLs to check.")
    #     broken_links = []
    #
    #     for url in urls:
    #         if url and "http" in url:
    #             try:
    #                 response = requests.head(url, timeout=10, verify=False, allow_redirects=True)
    #                 if response.status_code >= 400:
    #                     broken_links.append(f"{url} (Status: {response.status_code})")
    #                     print(f"-> Broken link found: {url} (Status: {response.status_code})")
    #             except requests.RequestException as e:
    #                 print(f"-> Could not check link {url}. Error: {e}")
    #
    #     if broken_links:
    #         warning_message = "WARNING: Found the following broken links:\n" + "\n".join(broken_links)
    #         print(warning_message)
    #     else:
    #         print("No broken links were found.")

