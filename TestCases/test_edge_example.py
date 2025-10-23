# import pytest
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.edge import EdgeChromiumDriverManager
#
#
# @pytest.fixture(scope="module")
# def edge_browser():
#     # Automatically downloads the correct msedgedriver and sets up the service
#     service = EdgeService(EdgeChromiumDriverManager().install())
#
#     # Initialize the Edge browser
#     driver = webdriver.Edge(service=service)
#
#     # Maximize the window for a better experience (optional)
#     driver.maximize_window()
#
#     # The 'yield' keyword makes this a teardown fixture
#     yield driver
#
#     # This code runs AFTER the test(s) are finished:
#     print("\nClosing Edge browser...")
#     driver.quit()
#
#
# def test_open_google_in_edge(edge_browser):
#     """
#     Test that opens Google in Edge, checks the title, and closes.
#     """
#     # 1. Instruct the Edge browser (from the fixture) to open a URL
#     edge_browser.get("https://www.google.com")
#
#     # 2. Add an assertion (the actual test logic)
#     # The browser's title should contain 'Google'
#     assert "Google" in edge_browser.title
#
#     # 3. You can also add a simple wait to see the browser before it closes (optional)
#     # import time; time.sleep(3)
#
#
# # You can add as many test functions as you like in this file.
# def test_another_website(edge_browser):
#     edge_browser.get("https://www.bing.com")
#     assert "Bing" in edge_browser.title