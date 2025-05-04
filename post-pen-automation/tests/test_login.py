import pytest
from pages.login_page import LoginPage
from config.credentials import TEST_EMAIL, TEST_PASSWORD
from data.test_data import TestData

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.login_page = LoginPage(page)

    def test_valid_login(self):
        self.login_page.navigate_to_login() \
            .enter_email(TEST_EMAIL) \
            .enter_password(TEST_PASSWORD) \
            .submit_form() \
            .verify_login_success()

    def test_invalid_password(self):
        with pytest.raises(Exception):
            self.login_page.navigate_to_login() \
                .enter_email(TEST_EMAIL) \
                .enter_password("wrongpassword") \
                .submit_form()