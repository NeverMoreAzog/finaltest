import time

from selenium.webdriver import Keys

from finaltest_1.base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait





class END_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    pick_qr_kod = "//*[@id='order-payment-options-wide']/label[1]/input"
    fill_FIO = "//*[@id='order-send-form']/div[1]/div[2]/label[1]/input"
    fill_phone = "//*[@id='order-send-form']/div[1]/div[10]/label/span[1]/input"
    fill_email = "//*[@id='order-send-form']/div[1]/div[12]/label/input"
    send_order = "//*[@id='order-submit']/span"
    # Getters

    def get_qr_kod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_qr_kod)))
    def get_fill_FIO(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.fill_FIO)))
    def get_fill_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.fill_phone)))
    def get_fill_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.fill_email)))
    def get_send_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.send_order)))

    # Actions

    def click_pick_qr_kod(self):
        self.get_qr_kod().click()
        print("Выбрали способ оплаты по QR коду")
    def input_FIO(self, value):
        self.get_fill_FIO().send_keys(value)
        print("Заполнили ФИО!")
    def input_phone(self, value):
        self.get_fill_phone().send_keys(value)
        print("Заполнили номер телефона!")
    def input_email(self, value):
        self.get_fill_email().send_keys(value)
        print("Заполнили Email!")
    def click_send_order(self):
        self.get_fill_email().click()
        print("НАЖАЛИ ОФОРМИТЬ ЗАКАЗ!")

    def end_buying(self):
        self.click_pick_qr_kod()
        self.input_FIO("Пупкин Иван Иванович")
        self.input_phone("8005553535")
        self.input_email("NeverMore@yandex.ru")
        # self.click_send_order()
        time.sleep(5)