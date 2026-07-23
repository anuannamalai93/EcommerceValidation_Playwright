import pytest

from Tests.blockads import blockads
from pageobjects.CartPage import CartPage
from pageobjects.LoginSignup import LoginSignup
from pageobjects.ProductsPage import Productspage
from pageobjects.TopMenu import TopMenu
import allure
from Tests.utils.testdata import get_test_data
@pytest.mark.skip(reason="to be completed")
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

