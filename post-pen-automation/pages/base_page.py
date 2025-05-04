from playwright.sync_api import Page
from utils.logging import logger
from config.config import TIMEOUT

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = TIMEOUT

    def navigate(self, url):
        self.page.goto(url)
        logger.info(f"Navigated to {url}")
        return self

    def fill(self, selector, text):
        self.page.fill(selector, text)
        logger.info(f"Filled {selector} with text")
        return self

    def click(self, selector):
        self.page.click(selector)
        logger.info(f"Clicked {selector}")
        return self

    def wait_for_selector(self, selector):
        self.page.wait_for_selector(selector, timeout=self.timeout)
        return self

    def get_text(self, selector):
        return self.page.text_content(selector)