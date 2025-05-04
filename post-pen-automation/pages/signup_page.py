# from pages.base_page import BasePage
# from config.config import BASE_URL
# from utils.common import generate_random_email

# class SignupPage(BasePage):
#     def __init__(self, page):
#         super().__init__(page)
#         self.full_name_input = "input#fullname"
#         self.email_input = "input#email"
#         self.password_input = "input#password"
#         self.submit_button = "button#submit-signup"
#         self.success_message = ".signup-success"

#     def navigate_to_signup(self):
#         self.navigate(f"{BASE_URL}/signup")
#         self.wait_for_selector(self.full_name_input)
#         return self

#     def enter_full_name(self, full_name):
#         self.fill(self.full_name_input, full_name)
#         return self

#     def enter_email(self, email=None):
#         email = email or generate_random_email()
#         self.fill(self.email_input, email)
#         return email

#     def enter_password(self, password):
#         self.fill(self.password_input, password)
#         return self

#     def submit_form(self):
#         self.click(self.submit_button)
#         return self

#     def verify_success(self):
#         self.wait_for_selector(self.success_message)
#         return self