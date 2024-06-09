import logging
import random
import string
from playwright.sync_api import sync_playwright

def generate_random_string(length=5):
    """Generate a random string of letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def click_and_fill(page, placeholder, text):
    """Click on the input field by placeholder and fill it with text."""
    input_field = page.get_by_placeholder(placeholder)
    input_field.click()
    input_field.fill(text)

def test_validate_menu_item_existence():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://qa-tipalti-assignment.tipalti-pg.com/index.html")

        menu_link = page.get_by_role("link", name="Menu")
        menu_link.click()

        menu_items = page.query_selector_all("nav a")

        menu_names = []
        for item in menu_items:
            text = item.text_content().strip()
            menu_names.append(text)

        # Remove the first and last items
        if menu_names:
            menu_names = menu_names[1:-1]

        logging.info("Filtered menu item names: %s", menu_names)

        assert "Kika" in menu_names, "'Kika' not found in the menu items"
        logging.info("Assertion passed: 'Kika' exists in the menu items.")

        page.pause()
        kika_link = page.locator("#menu").get_by_role("link", name="Kika")
        kika_link.click()
        page.pause()

        # Replace placeholders with random strings
        random_name = generate_random_string()
        random_email = generate_random_string() + "@aaa.aaa"
        random_message = generate_random_string()

        click_and_fill(page, "Name", random_name)
        click_and_fill(page, "Email", random_email)
        click_and_fill(page, "Message", random_message)

        send_button = page.get_by_role("button", name="Send")
        send_button.click()

        browser.close()

