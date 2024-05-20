# tests/test_github_login.py

import pytest
from playwright.sync_api import sync_playwright
import page_objects.login
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')
login_manager = LoginManager(config_path)
config = login_manager.config.config  # Accessing the config directly from LoginManager

class TestGithubLogin:
    @pytest.fixture(scope="class")
    def playwright_browser(self):
        with sync_playwright() as p:
            yield p

    @pytest.fixture(scope="class")
    def browser_context(self, playwright_browser):
        browser = playwright_browser.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        browser.close()

    @pytest.fixture(scope="class")
    def login_page(self, browser_context):
        page = browser_context.new_page()
        page.goto(config['github']['base_url'])
        yield page
        page.close()

    def test_verify_github_login(self, login_page):
        username, password, _ = login_manager.config.get_credentials()
        login_manager.perform_login(login_page, username, password)
        
        # Verify login success
        profile_icon = login_page.locator("avatar-user")
        assert profile_icon.is_visible(), "Login failed: Profile icon not visible"
