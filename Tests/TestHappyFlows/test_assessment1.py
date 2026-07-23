from Tests.blockads import blockads
from pageobjects.CartPage import CartPage
from pageobjects.LoginSignup import LoginSignup
from pageobjects.ProductsPage import Productspage
from pageobjects.TopMenu import TopMenu
import allure
from Tests.utils.testdata import get_test_data

@allure.title("End to End Happy flow")
@allure.description("Verifies that a guest user can search for products,"
                    "add the first two 'Sleeveless' items to the cart,"
                    "register during checkout, and successfully place an order.")
@allure.severity(allure.severity_level.CRITICAL)

def test_assessment1(page):

    testdata = get_test_data()

    page.route("**/*", blockads)
    page.goto(testdata["URL"])

    #object creation for required classes
    topmenu = TopMenu(page)
    productspage = Productspage(page)
    cartpage = CartPage(page)
    loginsignup = LoginSignup(page)

    topmenu.verify_home_page_loaded()
    topmenu.click_products()
    topmenu.verify_products_page_loaded()

    with allure.step("Search for Sleeveless Products"):
        searchstring = testdata["Assessment1"]["search"]["valid_product"]
        searchdata = productspage.search_product(searchstring)    #pass the search string into search_products method
    with allure.step("Add first 2 Sleeveless Products to Cart"):
        productspage.add_to_cart(searchstring, searchdata)        #call add_to_cart method to add first 2 sleeveless products to cart

    topmenu.click_cart()
    topmenu.verify_cart_page_loaded()

    cartpage.click_proceed_to_checkout()
    with allure.step("Verify Login/Register popup displayed"):
        cartpage.login_signup_from_checkout()
        topmenu.verify_signup_login_page_loaded()

    name = testdata["Assessment1"]["new_user"]["name"]
    email = testdata["Assessment1"]["new_user"]["email"]
    loginsignup.new_user_signup(name,email)
    loginsignup.verify_signup_page_loaded()
    user_data = testdata["Assessment1"]["user_data"]
    loginsignup.fill_signup_form(user_data)    #call fill_sign_up form method passing user data to create account

    topmenu.verify_home_page_loaded()
    topmenu.click_cart()
    topmenu.verify_cart_page_loaded()

    with allure.step("Proceed to cart after registering"):
        cartpage.click_proceed_to_checkout()
        cartpage.click_placeorder(productspage)
        card_details = testdata["Assessment1"]["card_details"]
        cartpage.payment(card_details)
    with allure.step("Purchase completed and invoice verified"):
        cartpage.verify_payment_confirmation()
        cartpage.download_invoice()



