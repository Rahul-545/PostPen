from pathlib import Path

BASE_URL = "https://postpen.ai/"  # Update with your actual domain
LOGIN_URL = "https://app.postpen.ai/auth?signup=true"    # Login page URL
SIGNUP_URL = "https://app.postpen.ai/auth"  # Signup page URL
BROWSER = "chromium"
HEADLESS = False
TIMEOUT = 30000

class PathConfig:
    SCREENSHOTS = Path("screenshots")
    LOGS = Path("logs")

    @classmethod
    def setup_dirs(cls):
        cls.SCREENSHOTS.mkdir(exist_ok=True)
        cls.LOGS.mkdir(exist_ok=True)

PathConfig.setup_dirs()