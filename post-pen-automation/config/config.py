from pathlib import Path

BASE_URL = "https://your-app-domain.com"  # Update with your actual domain
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