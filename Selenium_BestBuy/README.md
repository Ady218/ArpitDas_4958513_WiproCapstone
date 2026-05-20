# Selenium BestBuy Automation Framework

## Project Overview

This project is a Selenium Pytest Automation Framework developed for automating the BestBuy ecommerce website.

The framework follows the Page Object Model (POM) design pattern and includes:

- End-to-End Testing
- Positive Testing
- Negative Testing
- Data Driven Testing
- Logging
- Screenshot Capture
- HTML Reporting
- Allure Reporting

The framework automates major ecommerce workflows such as:
- Product navigation
- Product filtering
- Add to cart
- Checkout flow
- Invalid input handling
- Email validation testing

---

# Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Allure Reports
- Pytest HTML Reports
- OpenPyXL
- WebDriver Manager

---

# Framework Features

## Page Object Model (POM)
Separates:
- locators
- page methods
- test logic

for better maintainability and scalability.

---

## Data Driven Testing
Test data is managed through Excel sheets using OpenPyXL.

---

## Positive Testing
Validates expected application behavior with valid inputs.

---

## Negative Testing
Validates application behavior with invalid inputs and error handling.

---

## End-to-End Testing
Validates complete ecommerce business workflow from start to finish.

---

## Logging
Custom logger implementation for execution tracking.

---

## Screenshot Capture
Screenshots are captured automatically during test execution.

---

## Allure Reporting
Advanced graphical reporting with:
- screenshots
- execution history
- pass/fail analytics

---

# Project Structure

```bash
Selenium_BestBuy/
│
├── config/
│   └── config.properties
│
├── data/
│   └── testdata.xlsx
│
├── logs/
│   └── automation.log
│
├── pages/
│   ├── home_page.py
│   ├── macbook_page.py
│   ├── cart_page.py
│   └── __init__.py
│
├── reports/
│   ├── report.html
│   └── allure-results/
│
├── screenshots/
│
├── tests/
│   ├── test_end_to_end_flow.py
│   └── test_scenarios.py
│
├── utilities/
│   ├── excel_utils.py
│   ├── logger.py
│   └── read_properties.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md