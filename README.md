# Banking Automation Framework

## Project Overview

This is an End-to-End QA Automation Framework built for a banking application using Selenium with Python and Pytest. The framework automates core banking functionalities such as user registration, login, and fund transfer.

The framework is designed using the Page Object Model (POM) design pattern for better maintainability and scalability.

---

## Tech Stack

### Automation Tool

* Selenium (Python)

### Framework

* Pytest

### Design Pattern

* Page Object Model (POM)

### Reporting

* HTML Report

### Test Data

* Excel (Data Driven Testing)

### Logging

* Python Logging

### Parallel Execution

* Pytest-Xdist

### Configuration

* Config.ini

---

## Project Structure

Banking_Automation/
│── config/
│   │── config.ini
│
│── pages/
│   │── base_page.py
│   │── login_page.py
│   │── register_page.py
│   │── transfer_page.py
│   │── waits.py
│
│── tests/
│   │── test_login.py
│   │── test_register.py
│   │── test_transfer.py
│
│── testdata/
│   │── testdata.xlsx
│
│── utilities/
│   │── logger.py
│   │── read_data.py
│   │── screenshot.py
│
│── reports/
│── screenshots/
│── conftest.py
│── requirements.txt

---

## Features

* End-to-End Automation Testing
* Data Driven Testing using Excel
* Reusable Page Object Model
* Parallel Test Execution
* HTML Report Generation
* Screenshot Capture on Failure
* Logging Support
* Configurable Environment Setup

---

## Test Scenarios Covered

### Registration Module

* New user registration
* Validation of successful account creation

### Login Module

* Valid login verification
* Invalid login validation

### Transfer Module

* Fund transfer functionality validation

---

## Installation

Clone the repository:

git clone <your-repository-url>

Navigate to project folder:

cd Banking_Automation

Install dependencies:

pip install -r requirements.txt

---

## Run Tests

Run all tests:

pytest

Run tests in parallel:

pytest -n 3

Run with HTML report:

pytest --html=reports/report.html

---

## Future Enhancements

* Allure Reporting
* Jenkins Integration
* API Automation
* Database Validation (MySQL)
* Cross Browser Testing
* JSON/CSV Data Handling

---

## Author

Sai Kumar
QA Automation Engineer
