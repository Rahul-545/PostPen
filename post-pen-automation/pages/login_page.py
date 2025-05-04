from pages.base_page import BasePage
from config.config import BASE_URL

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = "input#email"
        self.password_input = "input#password"
        self.submit_button = "button#submit-login"
        self.dashboard_header = ".dashboard-header"

    def navigate_to_login(self):
        self.navigate(f"{BASE_URL}/login")
        self.wait_for_selector(self.email_input)
        return self

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