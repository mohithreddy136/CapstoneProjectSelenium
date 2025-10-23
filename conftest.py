# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# # Removed Firefox and Edge imports as they are no longer needed
# from selenium.webdriver.chrome.service import Service as ChromeService
# # Removed FirefoxService and EdgeService imports
# import os
# import time
#
# # Removed pytest_addoption function
# # Removed browser fixture
#
# # --- UPDATED ---
# # Removed the 'browser' parameter. This fixture now always launches Chrome.
# @pytest.fixture(scope="class")
# def setup_and_teardown(request):
#     """
#     This fixture sets up the Chrome browser before each test class
#     and tears it down afterward. It also takes a screenshot on failure.
#     """
#     print(f"\nSetting up the Chrome browser...")
#     driver = None
#
#     # --- UPDATED ---
#     # Launch Chrome directly. Removed the if/elif/else for other browsers.
#     try:
#         service = ChromeService(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service)
#         driver.maximize_window()
#         # Attach the driver to the class instance
#         request.cls.driver = driver
#     except Exception as e:
#         print(f"\n!!! Error during browser setup: {e} !!!")
#         pytest.fail(f"Browser setup failed: {e}")
#         # Ensure driver is None if setup fails partway
#         driver = None
#         request.cls.driver = None # Make sure class attribute is also None
#
#     # Yield control to the test function only if setup succeeded
#     if driver:
#         yield
#
#         # Teardown: This part runs after the tests in the class are complete
#         print("\n--- Starting Teardown ---") # DEBUG
#         # --- FIX ---
#         # Added 'hasattr' check. This prevents an AttributeError if a test fails
#         # during setup (before 'rep_call' is created) by checking if it exists first.
#         if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
#             print(f"DEBUG: Test '{request.node.name}' failed. Attempting screenshot...") # DEBUG
#             try:
#                 # --- MODIFIED --- Use the user-specified absolute path for the Screenshots folder
#                 screenshots_dir = r"C:\Users\Ascendion\SeleniumPytestFramework\Screenshots" # Using raw string for Windows path
#                 print(f"DEBUG: Screenshots directory path (hardcoded): {screenshots_dir}") # DEBUG
#
#                 if not os.path.exists(screenshots_dir):
#                     print(f"DEBUG: Creating directory: {screenshots_dir}") # DEBUG
#                     # Create the directory if it doesn't exist
#                     os.makedirs(screenshots_dir)
#                 else:
#                     print(f"DEBUG: Directory already exists: {screenshots_dir}") # DEBUG
#
#
#                 # Generate a unique filename for the screenshot
#                 timestamp = str(int(time.time()))
#                 # Extract class and method name for a more descriptive filename
#                 test_class_name = request.cls.__name__ if request.cls else "UnknownClass"
#                 test_method_name = request.node.name.split("::")[-1] # Get just the test method name
#
#                 # Use os.path.join for cross-platform compatibility
#                 screenshot_filename = f"{test_class_name}_{test_method_name}_{timestamp}.png"
#                 screenshot_path = os.path.join(screenshots_dir, screenshot_filename)
#                 print(f"DEBUG: Attempting to save screenshot to: {screenshot_path}") # DEBUG
#
#                 # --- NEW: Explicit check around save_screenshot ---
#                 try:
#                     print(f"DEBUG: *** BEFORE driver.save_screenshot() ***") # DEBUG
#                     driver.save_screenshot(screenshot_path)
#                     print(f"DEBUG: *** AFTER driver.save_screenshot() ***") # DEBUG
#                 except Exception as save_error:
#                     print(f"ERROR: Exception during driver.save_screenshot(): {save_error}") # DEBUG
#
#                 # Verify file exists after saving attempt
#                 if os.path.exists(screenshot_path):
#                      print(f"SUCCESS: Screenshot saved to: {screenshot_path}") # SUCCESS MESSAGE
#                 else:
#                      print(f"ERROR: Screenshot file NOT found at: {screenshot_path} after saving attempt!") # ERROR MESSAGE
#
#
#             except Exception as e:
#                 # This catches errors in path creation or filename generation
#                 print(f"Error during screenshot setup (path/filename): {e}") # Keep original error print
#
#         print(f"\nTearing down the Chrome browser...")
#         # Ensure driver exists before trying to quit
#         if driver:
#             driver.quit()
#         print("--- Teardown Complete ---") # DEBUG
#     else:
#         # If setup failed, yield wasn't reached, but we need to ensure teardown message appears if needed.
#         print("\nBrowser setup failed, skipping teardown actions.")
#
#
# # --- NEW ---
# # This hook runs after each test and stores the test result in the request node.
# # It is necessary for the screenshot-on-failure logic.
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # This magic ensures that the result of the test 'call' (the actual test execution)
#     # is available for the fixture teardown.
#     outcome = yield
#     rep = outcome.get_result()
#
#     # We only care about the 'call' phase (not setup or teardown) for failure screenshots
#     # We store the report on the item object for access in the fixture teardown
#     if rep.when == "call":
#         item.rep_call = rep
#

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
import os
import time


# --- NEW ---
# Add command-line options for browser and headless mode
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or edge")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")


@pytest.fixture(scope="class")
def setup_and_teardown(request):
    """
    Fixture that sets up the selected browser (Chrome/Edge) before each test class,
    and tears it down afterward. Also takes screenshots on failure.
    """
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    print(f"\nSetting up the browser: {browser_name} (headless={headless})...")
    driver = None

    try:
        if browser_name.lower() == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

        elif browser_name.lower() == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")
            service = EdgeService()
            driver = webdriver.Edge(service=service, options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver.maximize_window()
        request.cls.driver = driver

    except Exception as e:
        print(f"\n!!! Error during browser setup: {e} !!!")
        pytest.fail(f"Browser setup failed: {e}")
        driver = None
        request.cls.driver = None

    if driver:
        yield

        # --- TEARDOWN ---
        print("\n--- Starting Teardown ---")

        if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
            print(f"DEBUG: Test '{request.node.name}' failed. Taking screenshot...")

            try:
                screenshots_dir = r"C:\Users\Ascendion\SeleniumPytestFramework\Screenshots"
                if not os.path.exists(screenshots_dir):
                    os.makedirs(screenshots_dir)

                timestamp = str(int(time.time()))
                test_class_name = request.cls.__name__ if request.cls else "UnknownClass"
                test_method_name = request.node.name.split("::")[-1]
                screenshot_filename = f"{test_class_name}_{test_method_name}_{timestamp}.png"
                screenshot_path = os.path.join(screenshots_dir, screenshot_filename)

                try:
                    driver.save_screenshot(screenshot_path)
                    print(f"✅ Screenshot saved: {screenshot_path}")
                except Exception as save_error:
                    print(f"ERROR: Unable to save screenshot: {save_error}")

            except Exception as e:
                print(f"Error during screenshot setup: {e}")

        print("\nTearing down the browser...")
        if driver:
            driver.quit()
        print("--- Teardown Complete ---")
    else:
        print("\nBrowser setup failed, skipping teardown actions.")


# --- REQUIRED HOOK ---
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        item.rep_call = rep
