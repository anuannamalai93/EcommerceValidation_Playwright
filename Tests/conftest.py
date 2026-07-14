import pytest
from playwright.sync_api import Page

@pytest.fixture
def page(playwright):
    browser = playwright.chromium.launch(headless=False)  # launches browser engine
    context = browser.new_context()  # opens new context inside browser
    page = context.new_page()
    yield page
    page.close()
    #context.close()
    #browser.close()


class Context:
    pass

@pytest.fixture
def context():
    ctx = Context()
    return ctx