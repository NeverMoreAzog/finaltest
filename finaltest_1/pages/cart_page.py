import time

from selenium.webdriver import Keys

from finaltest_1.base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait





class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    value = "//*[@id='order-yandex-search-form-input']"
    next_next = "//*[@id='order-next']/span"

    # Getters

    def get_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value)))
    def get_next(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.next_next)))

    # Actions

    def click_delete_value(self):
        self.get_value().clear()
        print("Стёрли значения!")
    def input_value(self, value):
        self.get_value().send_keys(value)
        print("Ввели значение!")

    def press_enter(self):
        self.get_value().send_keys(Keys.RETURN)
        print("Нажали ENTER!")
    def click_next(self):
        self.get_next().click()
        print("Переходим на новую страницу!")

    def pick_cart(self):
        self.click_delete_value()
        self.input_value("Москва")
        self.press_enter()
        time.sleep(5)
        self.click_next()
        self.get_current_url()
        self.need_url('https://voronezh.nix.ru/scripts/order_cb_accompanying.html?step=adf489a5b156b4db4b2256f9a4d11a1e')