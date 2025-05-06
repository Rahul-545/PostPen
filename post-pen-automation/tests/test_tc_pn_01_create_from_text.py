# tests/test_tc_pn_01_create_from_text.py
import pytest
import time
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.create_post_page import CreatePostPage
from config.credentials import TEST_EMAIL, TEST_PASSWORD
from config.config import BASE_URL

@pytest.fixture
def logged_in_page(page):
    """Fixture to perform login before create post tests"""
    # Navigate to home
    home_page = HomePage(page)
    home_page.navigate(BASE_URL)  # Make sure this is implemented correctly
    
    # Login
    home_page.click_login_button()
    login_page = LoginPage(page)
    login_page.enter_email(TEST_EMAIL)
    login_page.enter_password(TEST_PASSWORD)
    login_page.submit_form()
    
    # Verify login success
    expect(page.locator("//img[@alt='postpen Logo']")).to_be_visible()
    
    # Navigate to create post page
    page.click("//span[normalize-space()='Create Post']")
    
    return page

def test_post_now_create_from_text(logged_in_page):
    """TC_PN_01: Post Now – Create from Text (default)
    
    Enter custom text in the editor, verify preview updates, 
    click Post Now, and verify success message or redirection.
    """
    page = logged_in_page
    create_post_page = CreatePostPage(page)
    
    # Ensure 'Create from text' is selected (it's the default)
    create_post_page.select_create_from_text()
    
    # Enter custom text
    test_content = "Quality testing is about finding the right problems to solve. #QA #Testing #BestPractices"
    create_post_page.enter_post_content(test_content)
    
    # Wait for preview to update
    time.sleep(2)
    
    # Verify preview shows the content
    create_post_page.verify_preview_content("Quality testing")
    create_post_page.verify_preview_content("#QA")
    
    # Post the content
    toast_message = create_post_page.post_now()
    assert "Content posted successfully" in toast_message, "Post success message did not appear as expected."
    # Verification is handled in post_now() method
    