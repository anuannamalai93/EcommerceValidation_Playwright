from playwright.sync_api import Page, expect
import time

class TopMenu:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.home_link = page.get_by_role("link", name="Home")
        self.products_link = page.locator(".material-icons.card_travel")
        self.cart_link =  page.locator("a[href='/view_cart']").first
        self.signup_login = page.get_by_role("link", name=" Signup / Login")
        self.logout_link = page.get_by_role("link", name="Logout")

    def click_home(self):
        self.home_link.click()
    def verify_home_page_loaded(self):
        expect(self.page).to_have_url("https://automationexercise.com/")

    def click_products(self):
        self.products_link.click()
    def verify_products_page_loaded(self):
        expect(self.page).to_have_url("https://automationexercise.com/products")

    def click_cart(self):
        expect(self.cart_link).to_be_visible()
        time.sleep(3)
        self.cart_link.click()
    def verify_cart_page_loaded(self):
        expect(self.page).to_have_url("https://automationexercise.com/view_cart")
        time.sleep(3)

    def click_signup_login(self):
        self.signup_login.click()
    def verify_signup_login_page_loaded(self):
        expect(self.page).to_have_url("https://automationexercise.com/login")

    def verify_logout_visible(self):
        expect(self.logout_link).to_be_visible()
    def verify_logout_not_visible(self):
        expect(self.logout_link).not_to_be_visible()
    def click_logout(self):
        self.logout_link.click()
    def verify_logout_page_loaded(self):
        expect(self.page).to_have_url("https://automationexercise.com/login")



