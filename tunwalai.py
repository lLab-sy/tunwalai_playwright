from playwright.sync_api import sync_playwright

def run(playwright):
    # Launch browser
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Navigate to the target website
    page.goto("https://example.com")

    # Wait for a specific element to load if needed
    page.wait_for_selector('h1')

    # Extract data (e.g., page title or content)
    page_title = page.title()
    main_heading = page.query_selector('h1').inner_text()

    print(f"Page Title: {page_title}")
    print(f"Main Heading: {main_heading}")

    # Close the browser
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
