class BasePage:
    def __init__(self, page):
        self.page = page

    async def navigate_to(self, url):
        await self.page.goto(url)

    async def wait_for_selector(self, selector):
        await self.page.wait_for_selector(selector)

    async def click(self, selector):
        await self.page.click(selector)

    async def fill(self, selector, value):
        await self.page.fill(selector, value)

    async def get_text(self, selector):
        return await self.page.text_content(selector)