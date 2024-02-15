import time

from selenium.webdriver import Keys

from finaltest_1.base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait





class Add_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    product_1 = "//*[@id='order-goods-frame']/div[2]/div/div/label[5]"
    product_2 = "//*[@id='order-goods-frame']/div[3]/div/div/label[7]"
    next_page = "//*[@id='order-next']/span"

    # Getters

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))
    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_2)))
    def get_next_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.next_page)))

    # Actions

    def click_product_1(self):
        self.get_product_1().click()
        print("Добавили батарейки!")
    def click_product_2(self):
        self.get_product_2().click()
        print("Добавили мышку!")
    def click_next_page(self):
        self.get_next_page().click()
        print("перешли на новую страницу!")

    def add_products(self):
        self.click_product_1()
        self.click_product_2()
        self.click_next_page()
        self.get_current_url()
        self.need_url('https://voronezh.nix.ru/scripts/order_cb.html?step=adf489a5b156b4db4b2256f9a4d11a1e')
        time.sleep(5)