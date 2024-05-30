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
        value = value_text.split(';')[-1].strip()
        logging.info(f"Extracted value: {value}")
        page.pause()
        values = []

        hover_locator = page.locator(".highcharts-point")

        for i in range(10):
            point = hover_locator.nth(i)
            point.hover()
            tooltip.wait_for(state='visible')
            value_text = tooltip.locator("td:has(span)").nth(1).inner_text()
            value = value_text.split(';')[-1].strip()
            values.append(value)
            logging.info(f"Extracted value from point {i + 1}: {value}")

        # Assert how many values start with 'c'
        c_count = sum(1 for v in values if v.lower().startswith('c'))
        logging.info(f"Number of values starting with 'c': {c_count}")
        assert c_count > 0, "No values start with 'c'"

        page.pause()

