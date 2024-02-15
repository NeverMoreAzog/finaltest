import time

from selenium import webdriver
from finaltest_1.pages.main_page import Main_page
from finaltest_1.pages.cart_page import Cart_page
from finaltest_1.pages.add_page import Add_page
from finaltest_1.pages.end_page import END_page



def test_buy_product_1(set_group):
    driver = webdriver.Firefox()

    bp = Main_page(driver)
    bp.buy_product()

    cr = Cart_page(driver)
    cr.pick_cart()

    add = Add_page(driver)
    add.add_products()

    end = END_page(driver)
    end.end_buying()

    time.sleep(10)
    driver.close()
