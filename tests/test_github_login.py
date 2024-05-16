from playwright.sync_api import sync_playwright

def goto_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://github.com/')
        #page.screenshot(path='example.png')
        page.pause()
        browser.close()

if __name__ == "__main__":
    goto_website()
