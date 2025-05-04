from playwright.sync_api import Page, sync_playwright

def configure_playwright():
    return {
        "use": {
            "headless": False,
            "viewport": {"width": 1280, "height": 720},
            "ignore_default_args": ["--disable-extensions"],
        },
        "timeout": 30000,
        "browser": "chromium",
        "base_url": "https://postpen.ai/",
    }

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page: Page = browser.new_page()
        page.goto("https://postpen.ai/")
        # Add any additional setup or teardown logic here
        browser.close()