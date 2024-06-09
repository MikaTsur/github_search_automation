# C:\Users\morellyo\Desktop\python\automation_tests\tests\test_dynamic.py
import logging
import requests
from datetime import datetime
from playwright.sync_api import sync_playwright


def test_api_dy_only():
    logging.info('Start the test')

    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    logging.info(f"POST request data: {data}")

    response = requests.post('https://api.restful-api.dev/objects', json=data,
                             headers={'Content-Type': 'application/json'})

    logging.info(f"POST response status: {response.status_code}")
    logging.info(f"POST response data: {response.json()}")
    assert response.status_code == 200

    response_json = response.json()
    item_id = response_json.get('id')
    created_at = response_json.get('createdAt')

    logging.info(f"Created item id: {item_id}")
    logging.info(f"Created at: {created_at}")

    delete_response = requests.delete(f'https://api.restful-api.dev/objects/{item_id}')
    logging.info(f"DELETE response status: {delete_response.status_code}")

    get_response = requests.get(f'https://api.restful-api.dev/objects/{item_id}')
    logging.info(f"GET response status after delete: {get_response.status_code}")

    second_delete_response = requests.delete(f'https://api.restful-api.dev/objects/{item_id}')
    logging.info(f"Second DELETE response status: {second_delete_response.status_code}")
    assert second_delete_response.status_code == 404, f"Item with id {item_id} should not be deletable twice"


def test_table():
    with (sync_playwright() as p):
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://en.wikipedia.org/wiki/Tom_Hanks")
        citizenship_selector = 'tr:has(th:has-text("Citizenship")) td .hlist ul li'

        citizenship_elements = page.locator(citizenship_selector).all_text_contents()

        assert len(citizenship_elements) == 2, f"Expected 2 citizenships, but found {len(citizenship_elements)}"

        logging.info(f'Citizenship elements: {citizenship_elements}')