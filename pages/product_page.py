import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class ProductPage(Base):
    url = "https://upstore24.ru/product/applewatch_se2022_40mm_al-sport_midnight"

    def __init__(self, driver, selected_specs):
        super().__init__(driver)
        self.driver = driver
        self.selected_specs = selected_specs

    # Locators

    name_product = "//h1[@class='product-title']"
    price_product = "//span[@class='product-price product-price--sale js-product-price']"
    to_cart_button = "//button[@class='button button--primary button--block button--medium']"
    specs_brand = "(//dd[@class='col-6'])[1]"
    specs_color = "(//dd[@class='col-6'])[2]"
    specs_system = "(//dd[@class='col-6'])[4]"
    specs_processor = "(//dd[@class='col-6'])[5]"
    specs_display_type = "(//dd[@class='col-6'])[6]"
    specs_display_size = "(//dd[@class='col-6'])[7]"
    specs_nfc = "(//dd[@class='col-6'])[9]"
    specs_defender = "(//dd[@class='col-6'])[10]"
    cart_button = "//a[@class='button button--primary button--block button--large']"

    # Getters

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.to_cart_button)))

    def get_specs_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.specs_brand)))

    def get_specs_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.specs_color)))

    def get_specs_system(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.specs_system)))

    def get_specs_processor(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.specs_processor)))

    def get_specs_display_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.specs_display_type)))

    def get_specs_display_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.specs_display_size)))

    def get_specs_nfc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.specs_nfc)))

    def get_specs_defender(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.specs_defender)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    # Actions

    def check_product_name(self):
        name = self.get_name_product()
        print(f"Chose Product name : {name.text}")
        return name.text

    def check_product_price(self):
        price = self.get_price_product()
        print(f"Chose Price product: {price.text}")
        return price.text

    def click_to_cart_button(self):
        self.get_to_cart_button().click()

    def check_specs_brand(self):
        brand = self.get_specs_brand()
        print(f"Chose Specs brand: {brand.text}")
        return brand.text

    def check_specs_color(self):
        color = self.get_specs_color()
        print(f"Chose Specs color: {color.text}")
        return color.text

    def check_specs_system(self):
        system = self.get_specs_system()
        print(f"Chose Specs system: {system.text}")
        return system.text

    def check_specs_processor(self):
        processor = self.get_specs_processor()
        print(f"Chose Specs processor: {processor.text}")
        return processor.text

    def check_specs_display_type(self):
        display_type = self.get_specs_display_type()
        print(f"Chose Specs display type: {display_type.text}")
        return display_type.text

    def check_specs_display_size(self):
        display_size = self.get_specs_display_size()
        print(f"Chose Specs display size: {display_size.text}")
        return display_size.text

    def check_specs_nfc(self):
        nfc = self.get_specs_nfc()
        print(f"Chose Specs nfc: {nfc.text}")
        return nfc.text

    def check_specs_defender(self):
        defender = self.get_specs_defender()
        print(f"Chose Specs defender: {defender.text}")
        return defender.text

    def click_cart_button(self):
        time.sleep(1)
        self.get_cart_button().click()

    # Methods

    def assert_product_specs(self):
        """Метод проверки совпадения описания товара в карточке с фильтрами"""
        assert self.check_product_name() == self.selected_specs["name"]
        assert self.check_product_price() == self.selected_specs["price"]
        assert self.check_specs_brand() == self.selected_specs["brand"]
        assert self.check_specs_color() == self.selected_specs["color"]
        assert self.check_specs_system() == self.selected_specs["system"]
        assert self.check_specs_processor() == self.selected_specs["processor"]
        assert self.check_specs_display_type() == self.selected_specs["display_type"]
        assert self.check_specs_display_size() == self.selected_specs[
            "display_size_1"] or self.check_specs_display_size() == self.selected_specs["display_size_2"]
        assert self.check_specs_nfc() == self.selected_specs["nfc"]
        assert self.check_specs_defender() == self.selected_specs["defender"]
        print("ALL CHOSE DETAILS OK\n")

    def enter_cart(self):
        """Метод добавления товара в корзину"""
        self.get_current_url()
        self.click_to_cart_button()
        self.click_cart_button()
        print("ENTER CART\n")
