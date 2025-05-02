class PostPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.post_input_selector = 'textarea[name="post"]'
        self.submit_button_selector = 'button[type="submit"]'

    async def create_post(self, content):
        await self.page.fill(self.post_input_selector, content)
        await self.page.click(self.submit_button_selector)