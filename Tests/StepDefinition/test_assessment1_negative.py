from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import context

from Tests.blockads import blockads
from pageobjects import CartPage
from pageobjects.LoginSignup import LoginSignup
from pageobjects.TopMenu import TopMenu
from pageobjects.ProductsPage import Productspage
from pageobjects.CartPage import CartPage
import allure
from Tests.utils.testdata import get_test_data

scenarios("../Features/assessment1_negative.feature")

@allure.epic("E-commerce")

@given("the user is on the products page")
def navigate_to_products_page(page: Page, context):
    context.testdata = get_test_data()
    context.page = page
    page.route("**/*", blockads)
    page.goto(context.testdata["URL"])

    #object creation for required classes
    context.topmenu = TopMenu(page)
    context.productspage = Productspage(page)
    context.cartpage = CartPage(page)
    context.loginsignup = LoginSignup(page)

    with allure.step("Navigate to Products page"):
        context.topmenu.verify_logout_not_visible()  # makes sure user is not logged in - requirement
        context.topmenu.verify_home_page_loaded()
        context.topmenu.click_products()
        context.topmenu.verify_products_page_loaded()


@when("the user searches for junk value")
def search_product(page: Page, context):
    allure.dynamic.title("Invalid search")
    allure.dynamic.description(
        "Validates that search displays zero results with invalid search text")
    with allure.step("Search for junk value in products search"):
        allure.dynamic.title("Invalid search")
        allure.dynamic.description("Validates that the search does not give any result with junk value")
        allure.dynamic.severity(allure.severity_level.NORMAL)
        context.searchstring = context.testdata["Assessment1"]["search"]["invalid_product"]
        context.searchdata = None


@then("the search results should not fetch any product")
def search_results(context):
    with allure.step("Verify empty search results"):
        context.searchdata = context.productspage.search_product(context.searchstring)
        assert context.searchdata.count() == 0, "Invalid search results"


@given("the user searches for sleeveless adds first 2 products to the cart")
def add_products_to_cart(context):
    with allure.step("Search for 'Sleeveless' products"):
        context.searchstring = context.testdata["Assessment1"]["search"]["valid_product"]
        context.searchdata = context.productspage.search_product(context.searchstring)
        context.productspage.add_to_cart(context.searchstring, context.searchdata)


@given("proceeds to checkout")
def proceed_to_checkout(context):
    with allure.step("Proceed to cart"):
        context.topmenu.click_cart()
        context.topmenu.verify_cart_page_loaded()
        context.cartpage.click_proceed_to_checkout()


@when("the user registers with an existing email")
def register_existing_user(context):
    allure.dynamic.title("Register with Existing User")
    allure.dynamic.description(
        "Validates that duplicate user registration is prevented by displaying an appropriate error message."
    )
    context.cartpage.login_signup_from_checkout()
    context.topmenu.verify_signup_login_page_loaded()


@then("the user should see an error message indicating that the email is already in use")
def verify_existing_user_error(context):
    with ((allure.step("Verify existing user message on using registered mail id"))):
        existing_user = context.testdata["Assessment1"]["existing_user"]
        context.loginsignup.register_existing_user(existing_user["name"],existing_user["email"])
