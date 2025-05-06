# tests/test_tc_pn_02_create_with_ai.py
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
    # Same fixture implementation as above
    home_page = HomePage(page)
    home_page.navigate(BASE_URL)
    
    home_page.click_login()
    login_page = LoginPage(page)
    login_page.enter_email(TEST_EMAIL)
    login_page.enter_password(TEST_PASSWORD)
    login_page.submit_form()
    
    expect(page.locator("//img[@alt='postpen Logo']")).to_be_visible()
    
    page.click("//span[normalize-space()='Create Post']")
    
    return page

def test_post_now_create_with_ai(logged_in_page):
    """TC_PN_02: Post Now – Create from Text with AI Content
    
    Write a short prompt, click Generate with AI, verify 
    generated content and preview, click Post Now, and validate success.
    """
    page = logged_in_page
    create_post_page = CreatePostPage(page)
    
    # Ensure 'Create from text' is selected
    create_post_page.select_create_from_text()
    
    # Enter prompt for AI generation
    prompt = "Write a short post about the importance of automated testing in software development."
    create_post_page.enter_post_content(prompt)
    
    # Generate content with AI
    create_post_page.generate_with_ai()
    
    # Verify that AI content was generated and is longer than original prompt
    editor_content = page.locator(create_post_page.TEXT_EDITOR_SELECTOR).text_content()
    assert len(editor_content) > len(prompt), "AI didn't generate expanded content"
    
    # Wait for preview to update
    time.sleep(2)
    
    # Verify preview contains content
    preview_text = page.locator(create_post_page.LINKEDIN_PREVIEW_SELECTOR).text_content()
    assert len(preview_text) > 0, "LinkedIn preview is empty"
    
    # Post the AI generated content
    create_post_page.post_now()
    
    # Verification is handled in post_now() method
