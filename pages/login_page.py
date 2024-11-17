from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from base.base_class import Base


class GeneratorUser:
    """Класс генерации юзера"""

    def __init__(self):
        self.faker = Faker('ru_RU')

    def generate_full_name(self):
        return self.faker.last_name() + ' ' + self.faker.first_name() + ' ' + self.faker.middle_name()

    def generate_phone(self):
        return self.faker.phone_number()

    def generate_email(self):
        return self.faker.email()

    def generate_password(self):
        return self.faker.password()


class LoginPage(Base):
    url = "https://upstore24.ru/client_account/login"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.user_generator = GeneratorUser()
        self.user_data = {}

    # Locators

    registration_button = "(//a[@class='co-button co-button--link co-form-button'])[2]"
    register_fullname = "//input[@id='client_contact_name']"
    register_phone = "//input[@id='client_phone']"
    register_email = "//input[@id='client_email']"
    register_password = "//input[@id='client_password']"
    register_confirm_password = "//input[@id='client_password_confirmation']"
    register_end_registration_button = "//button[@class='co-button co-form-button js-co-login-submit']"
    exit_button = "(//a[@class='co-menu-link co-menu-link--personal co-link'])[4]"

    login_email = "//input[@id='email']"
    login_password = "//input[@id='password']"

    # Getters

    def get_registration_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.registration_button)))

    def get_input_full_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.register_fullname)))

    def get_input_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.register_phone)))

    def get_input_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.register_email)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.register_password)))

    def get_input_confirm_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.register_confirm_password)))

    def get_register_end_registration_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.register_end_registration_button)))

    def get_exit_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.exit_button)))

    def get_login_email(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_email)))

    def get_login_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_password)))

    # Actions

    def click_registration_button(self):
        self.get_registration_button().click()
        print("Click registration button")

    def input_full_name(self, register_fullname):
        self.get_input_full_name().send_keys(register_fullname)
        print("Input full name")

    def input_phone(self, register_phone):
        self.get_input_phone().send_keys(register_phone)
        print("Input phone")

    def input_email(self, register_email):
        self.get_input_email().send_keys(register_email)
        print("Input email")

    def input_password(self, register_password):
        self.get_input_password().send_keys(register_password)
        print("Input password")

    def input_confirm_password(self, register_password):
        self.get_input_confirm_password().send_keys(register_password)
        print("Input confirmation password")

    def click_end_registration_button(self):
        self.get_register_end_registration_button().click()
        print("Click end registration button")

    def click_exit_button(self):
        self.get_exit_button().click()
        print("Click exit button")

    def input_login_email(self, login_email):
        self.get_login_email().send_keys(login_email)
        print("Input login email")

    def input_login_password(self, login_password):
        self.get_login_password().send_keys(login_password)
        print("Input login password")

    # Methods

    def registration(self):
        """Метод регистрации"""
        print("START REGISTRATION")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_registration_button()

        # Generation registration data
        register_fullname = self.user_generator.generate_full_name()
        register_email = self.user_generator.generate_email()
        register_phone = self.user_generator.generate_phone()
        register_password = self.user_generator.generate_password()

        # Save registration data
        self.user_data["full_name"] = register_fullname
        self.user_data["email"] = register_email
        self.user_data["phone"] = register_phone
        self.user_data["password"] = register_password

        # Use registration data
        self.input_full_name(register_fullname)
        self.input_phone(register_phone)
        self.input_email(register_email)
        self.input_password(register_password)
        self.input_confirm_password(register_password)

        self.click_end_registration_button()
        self.click_exit_button()
        print("END REGISTRATION \n")

    def authorization(self):
        """Метод авторизации"""
        print("START AUTHORIZATION")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_login_email(self.user_data["email"])
        self.input_login_password(self.user_data["password"])
        self.click_end_registration_button()
        print("END AUTHORIZATION \n")
