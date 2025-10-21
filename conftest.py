import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
from datetime import datetime


@pytest.fixture(scope="class")
def setup_and_teardown(request):
    """
    This fixture sets up the browser, runs the test, and then tears down the browser.
    If a test fails, it will take a screenshot.
    """
    print("\nSetting up the browser...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    request.cls.driver = driver

    # --- Allure Integration Hook ---
    # This makes the driver instance available to the pytest_runtest_makereport hook
    request.node.driver = driver

    yield

    print("\nTearing down the browser...")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    This hook captures the test result and takes a screenshot on failure.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        print(f"Test failed: {item.name}")
        driver = getattr(item, "driver", None)
        if driver:
            # Create screenshots directory if it doesn't exist
            screenshots_dir = "Screenshots"
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)

            # Generate a unique filename with a timestamp
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}_{now}.png")

            # Save the screenshot
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to: {screenshot_path}")

