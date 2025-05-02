import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.mark.login
def test_login(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    # Replace with actual credentials
    username = "test_user"
    password = "test_password"
    
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.submit()

    # Add assertions to verify successful login
    assert login_page.is_logged_in()  # Example assertion, implement this method in LoginPage

@pytest.mark.parametrize("username, password", [
    ("valid_user", "valid_password"),
    ("invalid_user", "invalid_password"),
])
def test_login_with_parametrization(page: Page, username, password):
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.submit()

    if username == "valid_user":
        assert login_page.is_logged_in()  # Example assertion for valid user
    else:
        assert login_page.is_login_failed()  # Example assertion for invalid user