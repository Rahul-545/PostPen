from pages.base_page import BasePage
from config.config import LOGIN_URL  # Add this to config.py

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = "//input[@id='email']"
        self.password_input = "//input[@id='password']"
        self.submit_button = "//button[@type='submit']"
        self.dashboard_header = "//img[@alt='PostPen Logo']"

    def verify_login_page_loaded(self):
        """Verify we're on login page without navigating"""
        self.wait_for_selector(self.email_input)
        assert LOGIN_URL in self.page.url  # Verify URL matches login page
        return self

    # Remove navigate_to_login() since we'll navigate via home page
    # Keep all other methods the same
    def enter_email(self, email):
        self.fill(self.email_input, email)
        return self

    def enter_password(self, password):
        self.fill(self.password_input, password)
        return self

    def submit_form(self):
        self.click(self.submit_button)
        return self

    def verify_login_success(self):
        self.wait_for_selector(self.dashboard_header)
        return self