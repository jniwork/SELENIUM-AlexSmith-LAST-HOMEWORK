import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(Base):
    url = "https://upstore24.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.selected_specs = {}

    # Locators

    product_type = "//span[contains(text(), 'Часы Apple Watch')]"
    price_slider = "//span[@class='irs-slider to']"
    brand_checkbox = "//label[@class='filter-value-label js-filter-value-label']"
    color_checkbox = "//label[contains(text(), 'Темная ночь')]"
    system_checkbox = "//label[contains(text(), 'на платформе watchOS')]"
    processor_checkbox = "//label[contains(text(), 'S8')]"
    display_type_checkbox = "//label[contains(text(), 'OLED')]"
    display_size_checkbox_1 = "//label[contains(text(), '1.6\"')]"
    display_size_checkbox_2 = "//label[contains(text(), '1.8\"')]"
    nfc_checkbox = "(//label[contains(text(), 'да')])[3]"
    defender_checkbox = "//label[contains(text(), 'WR50')]"
    order_by = "//select[@class='js-filter-sort input--sort']"
    product = "(//div[@class='product_card-title'])[2]"
    product_price = "(//span[@class='product_card-price product_card-price--sale'])[2]"

    # Getters

    def get_product_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_type)))

    def get_price_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider)))

    def get_brand_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_checkbox)))

    def get_color_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color_checkbox)))

    def get_system_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.system_checkbox)))

    def get_processor_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.processor_checkbox)))

    def get_display_type_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.display_type_checkbox)))

    def get_display_size_checkbox_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.display_size_checkbox_1)))

    def get_display_size_checkbox_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.display_size_checkbox_2)))

    def get_nfc_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.nfc_checkbox)))

    def get_defender_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.defender_checkbox)))

    def get_order_by(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_by)))

    def get_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))

    # Actions

    def click_product_type(self):
        time.sleep(1)
        self.get_product_type().click()
        print("Click product type")

    def edit_price_slider(self):
        time.sleep(1)
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_price_slider()).move_by_offset(-160, 0).release().perform()
        print("Edit price")

    def click_brand_checkbox(self):
        time.sleep(1)
        brand_cb = self.get_brand_checkbox()
        self.driver.execute_script("arguments[0].click();", brand_cb)
        self.selected_specs["brand"] = brand_cb.text
        print(f"Click brand checkbox : {brand_cb.text}")

    def click_color_checkbox(self):
        time.sleep(1)
        color_cb = self.get_color_checkbox()
        self.driver.execute_script("arguments[0].click();", color_cb)
        self.selected_specs["color"] = color_cb.text
        print(f"Click color checkbox : {color_cb.text}")

    def click_system_checkbox(self):
        time.sleep(1)
        system_cb = self.get_system_checkbox()
        self.driver.execute_script("arguments[0].click();", system_cb)
        self.selected_specs["system"] = system_cb.text
        print(f"Click system checkbox : {system_cb.text}")

    def click_processor_checkbox(self):
        time.sleep(1)
        processor_cb = self.get_processor_checkbox()
        self.driver.execute_script("arguments[0].click();", processor_cb)
        self.selected_specs["processor"] = processor_cb.text
        print(f"Click processor checkbox : {processor_cb.text}")

    def click_display_type_checkbox(self):
        time.sleep(1)
        display_type_cb = self.get_display_type_checkbox()
        self.driver.execute_script("arguments[0].click();", display_type_cb)
        self.selected_specs["display_type"] = display_type_cb.text
        print(f"Click display type checkbox : {display_type_cb.text}")

    def click_display_size_checkbox_1(self):
        time.sleep(1)
        display_size_cb = self.get_display_size_checkbox_1()
        self.driver.execute_script("arguments[0].click();", display_size_cb)
        self.selected_specs["display_size_1"] = display_size_cb.text
        print(f"Click display size checkbox 1 : {display_size_cb.text}")

    def click_display_size_checkbox_2(self):
        time.sleep(1)
        display_size_cb = self.get_display_size_checkbox_2()
        self.driver.execute_script("arguments[0].click();", display_size_cb)
        self.selected_specs["display_size_2"] = display_size_cb.text
        print(f"Click display size checkbox 2 : {display_size_cb.text}")

    def click_nfc_checkbox(self):
        time.sleep(1)
        nfc_cb = self.get_nfc_checkbox()
        self.driver.execute_script("arguments[0].click();", nfc_cb)
        self.selected_specs["nfc"] = nfc_cb.text
        print(f"Click NFC checkbox : {nfc_cb.text}")

    def click_defender_checkbox(self):
        time.sleep(1)
        defender_cb = self.get_defender_checkbox()
        self.driver.execute_script("arguments[0].click();", defender_cb)
        self.selected_specs["defender"] = defender_cb.text
        print(f"Click defender checkbox : {defender_cb.text}")

    def order_by_sale(self):
        time.sleep(1)
        order = self.get_order_by()
        self.driver.execute_script("arguments[0].click();", order)
        order.send_keys(Keys.END)
        order.send_keys(Keys.ENTER)

    def get_name(self):
        time.sleep(1)
        product_name = self.get_product()
        self.selected_specs["name"] = product_name.text
        print(f"Product name : {product_name.text}")
        return self.selected_specs["name"]

    def get_price(self):
        time.sleep(1)
        product_price = self.get_product_price()
        self.selected_specs["price"] = product_price.text
        print(f"Product price : {product_price.text}")
        return product_price

    def click_product(self):
        time.sleep(1)
        self.get_product().click()
        print("Click product")

    # Methods

    def chose_product(self):
        """Метод фильтрации и выбора товара"""
        print("START CHOSE PRODUCT")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_product_type()
        self.edit_price_slider()
        self.click_brand_checkbox()
        self.click_color_checkbox()
        self.click_system_checkbox()
        self.click_processor_checkbox()
        self.click_display_type_checkbox()
        self.click_display_size_checkbox_1()
        self.click_display_size_checkbox_2()
        self.click_nfc_checkbox()
        self.click_defender_checkbox()
        self.order_by_sale()
        self.get_name()
        self.get_price()
        self.click_product()
        print("END CHOSE PRODUCT\n")

    def get_selected_specs(self):
        """Метод возврата значений фильтров"""
        return self.selected_specs
