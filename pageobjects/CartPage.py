import re
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

class CartPage:
    # searchdata = None
    def __init__(self, page: Page):
        self.cart_total = ""
        self.page = page
        self.Download_invoice_button= self.page.get_by_role("link", name="Download Invoice")
        self.loginsignuplink= link = self.page.get_by_role("link", name="Register / Login")

    def click_proceed_to_checkout(self):
        self.page.locator("a.check_out").click(force=True)

    def login_signup_from_checkout(self):
        self.loginsignuplink.click()

    def click_placeorder(self, obj):
        #extract product names
        cart_products = []
        items = self.page.locator(".cart_description h4 a")
        for i in range(items.count()):
            cart_products.append(items.nth(i).inner_text())

        #verify products list
        products_list = obj.products_list()
        assert products_list == cart_products, "Products list doesn't match"
        print("Added products seen in cart")

        #extract cart final total value
        raw=self.page.locator("tr").last.locator(".cart_total_price").inner_text()
        self.cart_total=raw.replace("Rs. ", "").strip()

        #click on place order
        self.page.get_by_role("link", name= "Place Order").click()
        expect(self.page).to_have_url("https://automationexercise.com/payment")

    def payment(self, card_details):
        self.page.locator('[data-qa="name-on-card"]').fill(card_details["name"])
        self.page.locator('[data-qa="card-number"]').fill(card_details["card_number"])
        self.page.locator('[data-qa="cvc"]').fill(card_details["cvc"])
        self.page.locator('[data-qa="expiry-month"]').fill(card_details["expiry_month"])
        self.page.locator('[data-qa="expiry-year"]').fill(card_details["expiry_year"])
        self.page.get_by_role("button", name="Pay and Confirm Order").click()

    def verify_payment_confirmation(self):
        expect(self.page).to_have_url(re.compile("automationexercise.com/payment_done"))
        expect(self.page.locator('[data-qa="order-placed"]')).to_be_visible()
        expect(self.Download_invoice_button).to_be_visible()
        expect(self.page.locator('[data-qa="continue-button"]')).to_be_visible()

    def download_invoice(self):
        with self.page.expect_download() as download_info:
            self.Download_invoice_button.click()
        d = download_info.value
        invoice_file = "invoice.txt"
        d.save_as(invoice_file)
        with open(invoice_file, "r") as open_invoice:
            content = open_invoice.read()
        invoice_total = content.split("is ")[1].split(".")[0]
        assert self.cart_total == invoice_total, f"Mismatch! Page: {self.cart_total}, Invoice: {invoice_total}"
        print("invoice validated. Cart total matched.")


