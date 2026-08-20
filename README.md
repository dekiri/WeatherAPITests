# WeatherAI API Automation Framework

## Overview

This project is an API test automation framework developed to validate the WeatherAI API.

The framework focuses on:

- Functional API testing
- Positive and negative testing
- Input validation
- Boundary value testing
- Authentication testing
- Response validation
- Basic performance validation
- Automated HTML test reporting

The framework is designed to be reusable, maintainable, and easy to execute.

## API Under Test

**Base URL**

```text
https://api.weather-ai.co

Endpoint-GET /v1/weather

Documentation

https://weather-ai.co/docs#get-weather

Technology Stack
Tool	Purpose
Python	Programming language
Pytest	Test automation framework
Requests	HTTP/API client
python-dotenv	Environment configuration
pytest-html	HTML test reporting
Git	Version control
GitHub	Source code repository
Project Structure
weather-ai-api-automation/
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── reports/
│
├── test_data/
│   ├── __init__.py
│   └── weather_test_data.py
│
├── tests/
│   ├── __init__.py
│   ├── test_weather_happy_path.py
│   ├── test_weather_negative.py
│   ├── test_weather_authentication.py
│   ├── test_weather_parameters.py
│   └── test_weather_performance.py
│
├── utils/
│   ├── __init__.py
│   └── api_client.py
│
├── .env
├── .env.example
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
Prerequisites

The following are required:

Python 3.x
Pytest
Git
WeatherAI API key
Installation
1. Clone the repository
git clone <repository-url>

Navigate to the project:

cd weather-ai-api-automation
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment

Windows:

.venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
Configuration

Create a .env file in the project root:

BASE_URL=https://api.weather-ai.co
API_KEY=your_api_key_here

Replace your_api_key_here with your actual API key.

Security

The .env file contains sensitive credentials and must not be committed to GitHub.

The .env.example file can be used as a configuration template.

Running Tests

Run the complete test suite:

pytest -v

Run a specific test file:

pytest tests/test_weather_happy_path.py -v

Run tests with console output:

pytest -v -s
HTML Test Report

Generate an HTML report using:

pytest -v --html=reports/api-report.html --self-contained-html

The report will be generated at:

reports/api-report.html
Test Coverage

The framework covers:

Happy Path Testing
Valid latitude and longitude
Valid forecast days
Metric units
Imperial units
AI enabled
AI disabled
Negative Testing
Missing parameters
Invalid parameters
Invalid coordinates
Invalid authentication
Unsupported parameter values
Boundary Testing

Latitude:

-90
90
-91
91

Longitude:

-180
180
-181
181
Authentication Testing
Valid API key
Missing API key
Invalid API key
Response Validation

The framework validates:

HTTP status codes
Response headers
Content type
JSON response structure
Required response fields
Response data
Performance Testing

Basic API response-time validation is included to identify unusually slow responses.

Framework Design
API Client

utils/api_client.py

Handles:

API base URL
Authentication
HTTP requests
Request timeout
Reusable sessions
Configuration

config/settings.py

Handles:

Base URL
API key
API endpoint
Timeout configuration
Performance threshold
Test Data

test_data/

Contains reusable test data used by the automated tests.

Pytest Fixtures

conftest.py

Provides reusable test dependencies such as the API client.

Error Handling

The framework validates API behavior using:

HTTP status codes
Response bodies
Response structure
Error messages where applicable

Tests are designed based on the observed API contract rather than assuming that every invalid input must return a 4xx response.

Maintainability

The framework uses:

Reusable API client
Pytest fixtures
Parameterized tests
External configuration
Environment variables
Separate test data
Clear test naming
Centralized request handling
Security

API credentials are stored in environment variables rather than directly in test source code.

The .env file is excluded using .gitignore.

Only .env.example should be committed to source control.

Reporting

Pytest HTML reporting is used to provide:

Test execution summary
Passed tests
Failed tests
Execution duration
Failure details
Future Improvements

Potential improvements include:

JSON Schema validation
API contract testing
Enhanced logging
Retry handling
Allure reporting
Load testing
CI/CD integration
Expanded test coverage
Author

QA Automation Test Assignment

Built using Python and Pytest.

### Then preview it
After saving, press:

**`Ctrl + Shift + V`**

You'll see how the README will look when rendered.

And make sure the file is located here:

```text
weather-ai-api-automation/
└── README.md
