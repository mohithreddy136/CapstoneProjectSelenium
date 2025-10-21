Selenium Pytest Automation Framework

This project is a web automation framework built with Python, Selenium, and Pytest. It follows the Page Object Model (POM) design pattern for maintainable and scalable test automation.

Features

Selenium WebDriver: For browser automation.

Pytest: As the testing framework for test management and execution.

Page Object Model (POM): For separating UI elements from test logic.

Data-Driven Testing: Using openpyxl to read test data from Excel files.

Cross-Browser Testing: Configurable to run on different browsers.

Screenshots on Failure: Automatically captures screenshots when a test fails.

Allure Reports: For generating detailed and interactive test reports.

Markers: For grouping tests (e.g., smoke, regression).

Parameterized Testing: For running the same test with multiple data sets.

Project Structure

AutomationFramework/
├── PageObjects/
├── Screenshots/
├── TestData/
├── Tests/
├── Utilities/
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt


Setup and Installation

Clone the repository:

git clone <your-repository-url>
cd SeleniumPytestFramework


Create a virtual environment:

python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate


Install the dependencies:

pip install -r requirements.txt


Install Allure Commandline:
Follow the official installation guide for your operating system: https://allurereport.org/docs/gettingstarted-installation/

Running Tests

You can run tests using the pytest command from the root directory.

Run all tests:

pytest


Run tests from a specific file:

pytest Tests/test_010_Advanced_Features.py


Run tests with a specific marker:

pytest -m smoke


Run tests in parallel (requires pytest-xdist):

pytest -n 4  # Runs tests across 4 parallel processes


Allure Reports

This framework is integrated with Allure for rich reporting.

Generate Allure results:
Run your tests with the --alluredir flag to store the results.

pytest --alluredir=allure-results


Serve the Allure report:
Use the Allure command-line tool to generate and open the HTML report in your browser.

allure serve allure-results


This will open a local web server with a detailed, interactive report of the test execution.