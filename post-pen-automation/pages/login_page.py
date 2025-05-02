class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_selector = 'input[name="username"]'
        self.password_selector = 'input[name="password"]'
        self.login_button_selector = 'button[type="submit"]'

    async def enter_username(self, username):
        await self.page.fill(self.username_selector, username)

    async def enter_password(self, password):
        await self.page.fill(self.password_selector, password)

    async def submit_login(self):
        await self.page.click(self.login_button_selector)