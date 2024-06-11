
# Project Name
**PytestSelenium**

# Description
This project is a combination of UI, API, and mobile automation tests using Python-Selenium in the Pytest framework. It includes tests for various functionalities across different platforms.

# Prerequisites

###### Before running the tests, make sure you have the following installed:

1. Python (version 3.12.1)
2. Android Studio( 2023.2.1)
3. Appium(2.5.2)
4. Appium Inspector(2024.2.2)
5. IDE (PyCharm, VSCode, etc.)

Additionally, ensure you have the following setup:

# 1. Clone the Project: 
##  Clone the project repository from GitHub using the following command:
       git clone https://github.com/sharathshari6895/Pytest_E2E

# 2. Create a Virtual Environment:
##    Navigate to the project directory and create a virtual environment using the following command:
             	python -m venv venv

# 3. Activate the Virtual Environment:
	venv\Scripts\activate

# 4. Install Dependencies: Install the required dependencies by running the following command:
	pip install -r requirements.txt

# 5. Run the Tests: Execute the tests using the following command:
	pytest -s --alluredir=allure-report
	
# 6. View Test Reports: After running the tests, you can view the test reports using Allure. Run the following 	command to 
#     serve the reports:
	
	allure serve allure-report

