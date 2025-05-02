# config.py

class Config:
    BROWSER = "chromium"  # Options: chromium, firefox, webkit
    HEADLESS = False  # Set to True to run tests in headless mode
    TIMEOUT = 30000  # Timeout for actions in milliseconds
    BASE_URL = "https://www.linkedin.com"  # Base URL for LinkedIn