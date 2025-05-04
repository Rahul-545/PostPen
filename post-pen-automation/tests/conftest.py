import pytest
from playwright.sync_api import Playwright, sync_playwright
from config.config import BASE_URL, BROWSER, HEADLESS

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = getattr(p, BROWSER).launch(headless=HEADLESS)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()