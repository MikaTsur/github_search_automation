from playwright.sync_api import sync_playwright
import logging

def test_hover():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.statista.com/statistics/793628/worldwide-developer-survey-most-used-languages/")
        page.locator(".onetrust-pc-dark-filter").click()
        page.get_by_role("button", name="Accept all").click()

        page.locator(".highcharts-point").first.hover()
        tooltip = page.locator("table.tooltip")
        tooltip.wait_for(state='visible')
        value_text = tooltip.locator("td:has(span)").nth(1).inner_text()
        value = value_text.split(';')[-1].strip()  # Extract the numeric value
        logging.info(f"Extracted value: {value}")
        page.pause()

