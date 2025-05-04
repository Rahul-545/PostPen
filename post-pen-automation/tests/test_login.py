import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from config.credentials import TEST_EMAIL, TEST_PASSWORD

class TestLoginFlow:
    def test_successful_login(self, page):
        # Initialize pages
        home_page = HomePage(page)
        login_page = LoginPage(page)
        
        # 1. Navigate to home page
        home_page.navigate_to_home()
        
        # 2. Click login button (triggers navigation)
        home_page.click_login_button()
        
        # 3. Verify login page loaded
        login_page.verify_login_page_loaded()
        
        # 4. Perform login
        login_page.enter_email(TEST_EMAIL) \
                 .enter_password(TEST_PASSWORD) \
                 .submit_form() \
                 .verify_login_success()
        
        # Add any post-login assertions