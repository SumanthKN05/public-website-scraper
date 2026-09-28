
import sys
from playwright.sync_api import sync_playwright

def fetch_page(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        text = page.locator("body").inner_text()
        browser.close()
        return text

if __name__ == "__main__":
    url = sys.argv[1]
    print(fetch_page(url))
