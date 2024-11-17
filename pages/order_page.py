import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from base.base_class import Base


class OrderPage(Base):
    url = "https://upstore24.ru/new_order"

    def __init__(self, driver, selected_specs):
        super().__init__(driver)
        self.driver = driver
        self.selected_specs = selected_specs

    # Locators

    product = "//div[@class='co-basket_item-description']"
    product_price = "//div[@class='co-basket_total-price co-price--current']"
    fullname = "//input[@id='client_contact_name']"
    phone = "//input[@id='client_phone']"
    delivery = "//input[@id='shipping_address_full_locality_name']"
    address = "//textarea[@id='shipping_address_address']"
    comment = "//textarea[@id='order_comment']"
    create_order_button = "//button[@id='create_order']"

    # Getters

    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_comment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment)))

    def get_create_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.create_order_button)))

    # Actions

    def input_delivery(self):
        time.sleep(1)
        self.get_delivery().send_keys(
            Keys.CONTROL + "a" + Keys.BACKSPACE + "д Москва, Порховский район, Псковская обл." + Keys.ENTER)
        print("Input delivery")

    def input_comment(self):
        time.sleep(1)
        self.get_comment().send_keys("IT IS TEST!!!")
        print("Input comment")

    def input_address(self):
        time.sleep(1)
        self.get_address().send_keys("пр-кт Ленина, дом 15" + Keys.ENTER)
        print("Input address")

    def click_create_order_button(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.get_create_order_button().click()
        print("Create order")

    def get_product_name_info(self):
        return self.get_product_name().text

    def get_product_price_info(self):
        return self.get_product_price().text

    # Methods

    def assert_product_info(self):
        """Метод проверки названия и цены товара"""
        assert self.get_product_name_info() == self.selected_specs["name"]
        assert self.get_product_price_info() == self.selected_specs["price"]
        print("Product info correct\n")

    def create_order(self):
        """Метод слздания заказа"""
        self.get_current_url()
        self.input_delivery()
        self.input_address()
        self.input_comment()
        self.click_create_order_button()
        print("ORDER CREATE\n")
