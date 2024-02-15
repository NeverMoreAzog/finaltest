import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from finaltest_1.base.base_class import Base



class Main_page(Base):

    url = 'https://voronezh.nix.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_catalog = "//*[@id='toolbar-catalog']"
    pick_catalog = "//*[@id='content-wr']/div/div[2]/div[2]/div/div[2]/a[1]"
    pick_noyt_ASUS = "//*[@id='content-wr']/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div/div[3]/a"
    pick_filter_1 = "//*[@id='prm_996_3']"
    pick_filter_2 = "//*[@id='prm_993_68']"
    pick_filter_3 = "//*[@id='prm_4793_285']"
    pick_filter_4 = "// *[ @ id = 'prm_414_10']"
    # polzunok = "//*[@id='fs_prices']/div[2]/span[1]"
    pick_product = "//*[@id='search_results']/tbody/tr[4]/td[1]"
    buy = "//*[@id='add_to_cart']"
    cart = "//*[@id='toolbar-basket']"
    accept = "//*[@id='toolbar-basket-purchase']"
    close = "//*[@id='order-predialog-close-btn']"
    assert_word_1 = "//*[@id='order-client-options']/td[1]/span"

    # Getters

    def get_button_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_catalog)))
    def get_pick_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_catalog)))
    def get_noyt_ASUS(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_noyt_ASUS)))
    def get_pick_filter_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_filter_1)))
    def get_pick_filter_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_filter_2)))
    def get_pick_filter_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_filter_3)))
    def get_pick_filter_4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_filter_4)))
    # def get_polsunok(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.polsunok)))

    def get_pick_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_product)))
    def get_pick_buy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy)))
    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def get_accept(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept)))
    def get_close(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close)))
    def value_assert_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_word_1)))
    # Actions
    def assert_word(self, result):
        word = self.value_assert_word()
        assert result == word.text
        print("Мы на нужной странице!")
    def click_button_catalog(self):
        self.get_button_catalog().click()
        print("Выбрали каталог!")
    def click_pick_catalog(self):
        self.get_pick_catalog().click()
        print("Открыли каталог ноутбуков и ПК")
    def click_noyt_ASUS(self):
        self.get_noyt_ASUS().click()
        print("Выбрали ноутбук АСУС!")
    def click_pick_filter_1(self):
        self.get_pick_filter_1().click()
        print("Перешли на фильтр особенности!")

    def click_pick_filter_2(self):
        self.get_pick_filter_2().click()
        print("Перешли на фильтр OC!")
    def click_pick_filter_3(self):
        self.get_pick_filter_3().click()
        print("Перешли на фильтр процессор AMD модель!")
    def click_pick_filter_4(self):
        self.get_pick_filter_4().click()
        print("Перешли на фильтр Встроенная камера!")
    # def click_get_polsunok(self):
    #     self.actio
    #     print("Выбрали продукт!")
    def click_pick_product(self):
        self.get_pick_product().click()
        print("Выбрали продукт!")
    def click_button_buy(self):
        self.get_pick_buy().click()
        print("Нажали на кнопку купить!")
    def click_button_cart(self):
        self.get_button_cart().click()
        print("Нажали на корзину!")
    def click_button_accept(self):
        self.get_accept().click()
        print("Подтвердили заказ!")
    def click_button_close(self):
        self.get_close().click()
        print("Закрыли всплывающее окно!")

    def buy_product(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_button_catalog()
        self.click_pick_catalog()
        self.click_noyt_ASUS()
        self.click_pick_filter_1()
        self.click_pick_filter_2()
        self.click_pick_filter_3()
        time.sleep(5)
        self.click_pick_filter_4()
        time.sleep(3)
        self.click_pick_product()
        time.sleep(3)
        self.click_button_buy()
        self.click_button_cart()
        self.click_button_accept()
        self.click_button_close()
        self.get_current_url()
        self.assert_word("Оформление на:")
        # self.need_url("https://voronezh.nix.ru/scripts/order_cb_experimental.html#city_kladr_id=3600000100000&client=%D1%84%D0%B8%D0%B7&receiptPlace=shops&shop=23096")
        time.sleep(3)

