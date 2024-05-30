import logging
import string
import time

from playwright.sync_api import sync_playwright
import random


def generate_random_string(length=5):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def click_and_fill(page, placeholder, text):
    page.get_by_placeholder(placeholder).click()
    page.get_by_placeholder(placeholder).fill(text)


def test_table():
    with (sync_playwright() as p):
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://demoqa.com/webtables")

        page.get_by_role('button', name='Add').click()

        first_name = generate_random_string()
        last_name = generate_random_string()
        email = f"{generate_random_string()}@example.com"
        age = str(random.randint(18, 99))
        salary = str(random.randint(30000, 120000))
        department = generate_random_string()

        click_and_fill(page, "First Name", first_name)
        click_and_fill(page, "Last Name", last_name)
        click_and_fill(page, "name@example.com", email)
        click_and_fill(page, "Age", age)
        click_and_fill(page, "Salary", salary)
        click_and_fill(page, "Department", department)
        page.get_by_role('button', name='Submit').click()

        time.sleep(1)
        assert page.get_by_role('gridcell',
                                name=first_name).first.is_visible(), f"First Name {first_name} is not visible in the grid."
        assert page.get_by_role('gridcell',
                                name=last_name).is_visible(), f"Last Name {last_name} is not visible in the grid."
        assert page.get_by_role('gridcell', name=email).is_visible(), f"Email {email} is not visible in the grid."
        assert page.get_by_role('gridcell', name=age).is_visible(), f"Age {age} is not visible in the grid."
        assert page.get_by_role('gridcell', name=salary).is_visible(), f"Salary {salary} is not visible in the grid."
        assert page.get_by_role('gridcell',
                                name=department).is_visible(), f"Department {department} is not visible in the grid."

        logging.info(f"First Name {first_name} is visible in the grid.")
        logging.info(f"Last Name {last_name} is visible in the grid.")
        logging.info(f"Email {email} is visible in the grid.")
        logging.info(f"Age {age} is visible in the grid.")
        logging.info(f"Salary {salary} is not visible in the grid.")
        logging.info(f"Department {department} is not visible in the grid.")

# if __name__ == "__main__":
#     test_table()
