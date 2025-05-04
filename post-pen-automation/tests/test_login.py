import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from config.credentials import TEST_EMAIL, TEST_PASSWORD
import time


class TestLoginFlow:
    def test_successful_login(self, page):
        # Initialize pages
        home_page = HomePage(page)
        login_page = LoginPage(page)
        
        # 1. Navigate to home page
        home_page.navigate_to_home()
        time.sleep(2)  # Wait 2 seconds to see the home page
        
        # 2. Click login button (triggers navigation)
        home_page.click_login_button()
        time.sleep(2)  # Wait to see navigation effect
        
        # 3. Verify login page loaded
        login_page.verify_login_page_loaded()
        time.sleep(1)  # Wait to see the login page
        
        # 4. Perform login steps with delays
        login_page.enter_email(TEST_EMAIL)
        time.sleep(1)  # Wait to see email entered
        
        login_page.enter_password(TEST_PASSWORD)
        time.sleep(1)  # Wait to see password entered
        
        login_page.submit_form()
        time.sleep(2)  # Wait to see form submission
        
        login_page.verify_login_success()
        time.sleep(2)  # Wait to see successful login
        
        # 5. Post-login assertions
        assert page.url == "https://app.postpen.ai/dashboard", "Should redirect to dashboard after login"
        # assert page.is_visible("text=Welcome"), "Welcome message should be visible"
        time.sleep(3)  # Final wait to see the dashboard
