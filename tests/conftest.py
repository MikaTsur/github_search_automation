#automation_tests\tests\conftest.py
import pytest
from playwright.sync_api import sync_playwright
from config.config import Config

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def config():
    return Config('config/config.yaml')

