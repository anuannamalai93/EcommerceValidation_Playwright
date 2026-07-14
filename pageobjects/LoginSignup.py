from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page
import time


class LoginSignup:
    def __init__(self, page: Page):
        self.page = page

    def register_existing_user(self, name, email):
        self.page.locator(".signup-form").locator('[data-qa="signup-name"]').fill(name)
        self.page.locator(".signup-form").locator('[data-qa="signup-email"]').fill(email)
        self.page.get_by_role("button", name="Signup").click()
        expect(self.page.locator(".signup-form").locator("p")).to_have_text("Email Address already exist!")

    def new_user_signup(self, name, email):
        self.page.locator(".signup-form").locator('[data-qa="signup-name"]').fill(name)
        self.page.locator(".signup-form").locator('[data-qa="signup-email"]').fill(email)
        self.page.get_by_role("button", name="Signup").click()

    def verify_signup_page_loaded(self):
        expect(self.page).to_have_url("https://automationexercise.com/signup")

    def fill_signup_form(self, user):
        self.page.locator("#id_gender2").check()
        self.page.locator("#password").fill(user["password"])
        self.page.locator("#days").select_option(label=user["day"])
        self.page.locator("#months").select_option(label=user["month"])
        self.page.locator("#years").select_option(label=user["year"])
        self.page.locator("#first_name").fill(user["first_name"])
        self.page.locator("#last_name").fill(user["last_name"])
        self.page.locator("#address1").fill(user["address"])
        self.page.locator("#state").fill(user["state"])
        self.page.locator("#city").fill(user["city"])
        self.page.locator("#zipcode").fill(user["zipcode"])
        self.page.locator("#mobile_number").fill(user["mobile"])
        self.page.locator('[data-qa="create-account"]').click()
        expect(self.page.locator('[data-qa="account-created"]')).to_be_visible()
        self.page.locator('[data-qa="continue-button"]').click()

    def login(self, email, password):
        self.page.get_by_placeholder("Email Address").fill(email)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.locator('[data-qa="login-button"]').click()