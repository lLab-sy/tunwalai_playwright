from playwright.sync_api import sync_playwright
from datetime import date

def run(playwright):
    # Launch browser
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Navigate to the target website
    page.goto("https://www.tunwalai.com/story/type/topview?period=daily")

    # Wait for a specific element to load if needed
    page.wait_for_selector('div')

    # Extract data (e.g., page title or content)
    page_title = page.title()
    top3_content = page.query_selector_all('div.item.top3')

    current_date = date.today()
    print(f"Page Title: {page_title} at {current_date}")

    # rank:int, name:string, author:string, category:string
    novel_list = []
    for content in top3_content:
        rank = len(novel_list)+1
        name = content.query_selector('div.content-main-text').inner_text()
        author = content.query_selector('div.one-line-text.content-sub-text').inner_text()  
        category = content.query_selector('div.one-line-text.content-sub-sub-text').inner_text()
        print("-"*10)
        print(rank, name, author, category)
        novel_list.append({"rank": rank, "name": name, "author": author, "category": category, "date": current_date})

    other_content = page.query_selector_all('div.item.pt-16.pb-16.d-flex')
    for content in other_content:
        rank = content.query_selector('div.ranking-number').inner_text()
        name = content.query_selector('div.content-main-text').inner_text()
        author = content.query_selector('div.one-line-text.content-sub-text').inner_text()  
        category = content.query_selector('div.one-line-text.content-sub-sub-text').inner_text()  
        print("-"*10)
        print(rank, name, author, category)
        novel_list.append({"rank": rank, "name": name, "author": author, "category": category, "date": current_date})

    # Close the browser
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
