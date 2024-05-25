from playwright.sync_api import sync_playwright
import pytest
import requests
from bs4 import BeautifulSoup
import logging


# Test case using pytest
def test_login_functionality():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        response = requests.get('https://www.themarker.com/')
        if response.status_code == 200:
            logging.info('response 200')
            soup = BeautifulSoup(response.content, 'html.parser')
            target_span = soup.find('span', text="דולר-שקל רציף")
            if target_span:
                value_span = target_span.find_next('span')
                if value_span:
                    value = value_span.text
                    print(value)
                    logging.info(f'value is {value}')
                else:
                    print("Value span not found.")
            else:
                print("Target span not found.")
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

        browser.close()
