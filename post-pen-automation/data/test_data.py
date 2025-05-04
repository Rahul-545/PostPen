from utils.common import generate_random_email, generate_random_password

class TestData:
    VALID_FULLNAME = "Test User"
    VALID_EMAIL = "valid@example.com"
    VALID_PASSWORD = "ValidPass123!"
    INVALID_EMAIL = "invalid-email"
    SHORT_PASSWORD = "abc"
    
    @staticmethod
    def random_user():
        return {
            "fullname": "Test User",
            "email": generate_random_email(),
            "password": generate_random_password()
        }