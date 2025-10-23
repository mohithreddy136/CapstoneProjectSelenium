import os
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="module")
def edge_browser():
    """
    Pytest fixture that sets up and tears down the Edge browser.
    It first tries to use a locally available msedgedriver.exe (for offline use),
    and only downloads it if not found.
    """

    # Path where you can place msedgedriver.exe manually
    local_driver_path = r"C:\\Users\\Ascendion\\Downloads\\edgedriver_win64\\msedgedriver.exe"

    # Check if a local driver exists (helps when offline)
    if os.path.exists(local_driver_path):
        print(f"✅ Using local EdgeDriver: {local_driver_path}")
        service = EdgeService(local_driver_path)
    else:
        print("🌐 Downloading EdgeDriver using webdriver_manager...")
        try:
            service = EdgeService(EdgeChromiumDriverManager().install())
        except Exception as e:
            raise RuntimeError(
                "❌ Could not download EdgeDriver. "
                "Please ensure internet connection or place msedgedriver.exe at C:\\Drivers"
            ) from e

    # Initialize Edge browser
    driver = webdriver.Edge(service=service)
    driver.maximize_window()

    yield driver

    print("\nClosing Edge browser...")
    driver.quit()


def test_open_google_in_edge(edge_browser):
    """Open Google and verify title."""
    edge_browser.get("https://www.google.com")
    assert "Google" in edge_browser.title


def test_another_website(edge_browser):
    """Open Bing and verify title."""
    edge_browser.get("https://www.bing.com")
    assert "Bing" in edge_browser.title
