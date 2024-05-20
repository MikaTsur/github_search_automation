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
    url = config['github']['base_url']
except KeyError as e:
    print(f"Configuration key not found: {e}")
    exit(1)

def goto_github_search(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.pause()
        browser.close()