# pages/create_post_page.py
from pages.base_page import BasePage

from playwright.sync_api import Page, expect
import time

class CreatePostPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Content source options
        self.CREATE_FROM_TEXT_SELECTOR = "//button[normalize-space()='Continue with Text']"
        
        # Editor and AI generation
        self.TEXT_EDITOR_SELECTOR = "//div[@aria-label='Text editor for creating content']" # Update with actual selector
        self.GENERATE_WITH_A1_BUTTON = "//button[normalize-space()='Generate with AI']" # Update with actual button text
        
        # LinkedIn preview
        self.LINKEDIN_PREVIEW_SELECTOR = "//div[contains(@class,'text-sm whitespace-pre-wrap linkedln_content')]"
        
        # Action buttons
        self.POST_NOW_BUTTON = "//button[normalize-space()='Post Now']"
        
        # Success messages
        self.POST_SUCCESS_MESSAGE = "//div[contains(text(),'Content posted successfully')]" # Update with actual text
    
    def select_create_from_text(self):
        """Select the 'Create from text' option"""
        self.page.locator(self.CREATE_FROM_TEXT_SELECTOR).click()
    
    def enter_post_content(self, content):
        """Enter content in the text editor"""
        text_editor = self.page.locator(self.TEXT_EDITOR_SELECTOR)
        text_editor.click()
        text_editor.fill(content)
    
    def generate_with_a1(self):
        """Click the Generate with A1 button"""
        self.page.locator(self.GENERATE_WITH_A1_BUTTON).click()
        # Add wait for AI generation to complete
        self.page.wait_for_timeout(5000)  # Adjust timeout as needed for A1 generation
    
    def verify_preview_content(self, expected_content):
        """Verify that content appears in the LinkedIn preview"""
        preview = self.page.locator(self.LINKEDIN_PREVIEW_SELECTOR)
        expect(preview).to_contain_text(expected_content)
    
    def post_now(self):
        """Click the Post Now button"""
        self.page.locator(self.POST_NOW_BUTTON).click()
        # Wait for success message
        success_message = self.page.locator(self.POST_SUCCESS_MESSAGE)
        expect(success_message).to_be_visible(timeout=100000)
        return success_message.text_content()  # Longer timeout for posting
