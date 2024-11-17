from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from base.base_class import Base


class CartPage(Base):
    url = "https://upstore24.ru/product/applewatch_se2022_40mm_al-sport_midnight"

    def __init__(self, driver, selected_specs):
        super().__init__(driver)
        self.driver = driver
        self.selected_specs = selected_specs

    # Locators

    product = "//div[@class='cart-item-title']"
    product_price = "//span[@class='cart-order-total_price js-cart-order-total_price']"
    order_button = "//input[@value='Оформить заказ']"

    # Getters

    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    # Actions

    def get_product_name_info(self):
        return self.get_product_name().text

    def get_product_price_info(self):
        return self.get_product_price().text

    def click_order_button(self):
        self.get_order_button().click()


    # Methods

    def assert_product_info(self):
        """Метод проверки названия и цены товара"""
        assert self.get_product_name_info() == self.selected_specs["name"]
        assert self.get_product_price_info() == self.selected_specs["price"]
        print("Product info correct\n")

    def go_to_order(self):
        """Метод перехода в корзину"""
        self.get_current_url()
        self.get_order_button().click()
        print("Click order button\n")