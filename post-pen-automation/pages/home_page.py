from pages.base_page import BasePage
from config.config import BASE_URL

class HomePage(BasePage):
    LOGIN_BUTTON = "//span[normalize-space()='Log In']"  # Update with your actual selector
    
    def __init__(self, page):
        super().__init__(page)
    
    def navigate_to_home(self):
        self.navigate(BASE_URL)
        self.wait_for_selector(self.LOGIN_BUTTON)
        return self
    
    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)
        # No need to return current page since we're navigating away