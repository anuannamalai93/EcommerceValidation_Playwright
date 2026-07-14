from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page
import time


class Productspage:
    def __init__(self, page: Page):
        self.page = page
        self.added_products = []

    def search_product(self, searchstring):
        self.page.get_by_placeholder("Search Product").fill(searchstring)
        expect(self.page.locator("#submit_search")).to_be_visible()
        time.sleep(3)
        self.page.locator("#submit_search").click()
        time.sleep(5)
        # Wait for page to be ready - can show either "Searched Products" or "All Products"
        product_title = self.page.locator(".title.text-center")
        expect(product_title).to_be_visible(timeout=5000)
        # Return products regardless of whether search yielded results
        return self.page.locator(".product-image-wrapper")  # one per product

    def add_to_cart(self, searchstring, searchdata):
        for i in range(2):  # first 2 products
            selection = searchdata.nth(i)
            productname = selection.locator(".productinfo.text-center").locator("p").inner_text().strip()
            assert searchstring.lower() in productname.lower(), f"Expected product to contain '{searchstring}', but got '{productname}'"
            self.added_products.append(productname)
            selection.hover()  # triggers the overlay to render/become visible
            selection.locator(".product-overlay .add-to-cart").click()
            self.page.locator("button:has-text('Continue Shopping')").click()
            time.sleep(3)

    def products_list(self):
        return self.added_products
