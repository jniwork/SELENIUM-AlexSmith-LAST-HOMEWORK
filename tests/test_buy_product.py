from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_buy_product(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start Test Buy Product")

    lp = LoginPage(driver)
    lp.registration()
    lp.authorization()

    mp = MainPage(driver)
    mp.chose_product()
    selected_specs = mp.get_selected_specs()

    pp = ProductPage(driver, selected_specs)
    pp.assert_product_specs()
    pp.enter_cart()

    cp = CartPage(driver, selected_specs)
    cp.assert_product_info()
    cp.go_to_order()

    op = OrderPage(driver, selected_specs)
    op.assert_product_info()
    op.create_order()

    fp = FinishPage(driver)
    fp.get_current_url()
    fp.get_screenshot()
