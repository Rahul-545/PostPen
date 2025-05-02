import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.post_page import PostPage

@pytest.mark.usefixtures("setup")
class TestPostCreation:

    def test_create_post(self, page: Page):
        login_page = LoginPage(page)
        post_page = PostPage(page)

        # Navigate to login page and log in
        login_page.navigate()
        login_page.enter_username("test_user")
        login_page.enter_password("test_password")
        login_page.submit()

        # Create a new post
        post_page.navigate()
        post_page.enter_post_content("This is a test post.")
        post_page.submit_post()

        # Verify the post was created successfully
        assert post_page.is_post_created("This is a test post.")