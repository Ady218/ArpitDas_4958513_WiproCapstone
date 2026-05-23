# 🛒 BDD_BestBuy Automation Framework

## 📌 Project Overview

BDD_BestBuy is a Hybrid Test Automation Framework developed using:

- Python
- Selenium
- Behave (BDD)
- Page Object Model (POM)
- Allure Reporting
- Excel Driven Testing

This framework automates multiple BestBuy ecommerce scenarios including:

- Positive Flows
- Negative Flows
- Checkout Validations
- Navigation Validations

The framework generates detailed Allure Reports with:

- Step-wise execution
- Screenshots
- Logs
- Assertions
- Execution status

---

# 🚀 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Selenium | Web Automation |
| Behave | BDD Framework |
| Allure | Reporting |
| OpenPyXL | Excel Data Handling |
| WebDriver Manager | Driver Management |
| Logging | Execution Logs |

---

# 📂 Project Structure

```text
BDD_BestBuy/
│
├── config/
│   └── config.ini
│
├── data/
│   └── testdata.xlsx
│
├── features/
│   │
│   ├── steps/
│   │   ├── __init__.py
│   │   ├── end_to_end_steps.py
│   │   └── test_scenarios_steps.py
│   │
│   ├── end_to_end.feature
│   ├── test_scenarios.feature
│   └── environment.py
│
├── logs/
│   └── automation.log
│
├── pages/
│   ├── __init__.py
│   ├── cart_page.py
│   ├── home_page.py
│   └── macbook_page.py
│
├── reports/
│   ├── allure-report/
│   ├── allure-results/
│   └── screenshots/
│
├── utilities/
│   ├── __init__.py
│   ├── allure_logs.py
│   ├── excel_utils.py
│   ├── logger.py
│   ├── read_properties.py
│   └── screenshot.py
│
├── behave.ini
├── README.md
└── requirements.txt