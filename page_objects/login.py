import configparser
import os
from playwright.sync_api import sync_playwright

# Construct the correct path to the config file
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')

# Read configuration
config = configparser.ConfigParser()
config.read(config_path)

try:
    # Extract values
    username = config['github']['username']
    password = config['github']['password']
    base_url = config['github']['base_url']
except KeyError as e:
    print(f"Configuration key not found: {e}")
    exit(1)

def goto_website(username, password, base_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(base_url)
        perform_login(page, username, password)
        page.pause()
        browser.close()

def perform_login(page, username, password):
    page.get_by_role("link", name="Sign in").click()
    page.get_by_label("Username or email address").click()
    page.get_by_label("Username or email address").fill(username)
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Sign in", exact=True).click()

if __name__ == "__main__":
    goto_website(username, password, base_url)
