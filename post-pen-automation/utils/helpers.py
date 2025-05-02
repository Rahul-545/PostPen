# helpers.py

def format_post_content(content):
    """Format the post content for LinkedIn."""
    return content.strip()

def validate_credentials(username, password):
    """Validate the provided username and password."""
    return bool(username) and bool(password)

def log_error(message):
    """Log an error message."""
    print(f"ERROR: {message}")

def log_info(message):
    """Log an informational message."""
    print(f"INFO: {message}")