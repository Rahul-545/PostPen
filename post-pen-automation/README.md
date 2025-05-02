# README.md

# Post Pen Automation

Post Pen is a QA automation tool designed to facilitate posting multiple updates on LinkedIn by integrating user accounts. This project utilizes Python with Playwright, following the Page Object Model (POM) design pattern.

## Project Structure

```
post-pen-automation
├── config
├── data
├── pages
├── tests
├── utils
├── .gitignore
├── playwright.config.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd post-pen-automation
   ```

2. **Install dependencies:**
   Make sure you have Python 3.7 or higher installed. Then, install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Playwright:**
   Run the following command to install the necessary browser binaries:
   ```bash
   playwright install
   ```

4. **Run Tests:**
   You can run the test suite using pytest:
   ```bash
   pytest
   ```

## Usage Guidelines

- The `config/config.py` file contains configuration settings for Playwright, including browser options and timeout settings.
- The `data/test_data.json` file holds sample test data for login credentials and post content.
- The `pages` directory contains page classes that encapsulate the functionality of the application.
- The `tests` directory includes test cases for the login functionality and post creation.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.