from playwright.sync_api import sync_playwright

def goto_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://github.com/')
        perform_login(page)
        page.pause()
        browser.close()

def perform_login(page):
    page.get_by_role("link", name="Sign in").click()
    page.get_by_label("Username or email address").click()
    page.get_by_label("Username or email address").fill("mikatsurtest")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Github-1!")
    page.get_by_role("button", name="Sign in", exact=True).click()

if __name__ == "__main__":
    goto_website()
