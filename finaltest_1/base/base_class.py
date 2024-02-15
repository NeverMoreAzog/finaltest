
class Base:
    def __init__(self, driver):
        self.driver = driver

    def need_url(self, result):
        get_url = self.driver.current_url
        assert result == get_url
        print("Мы на нужной странице!")

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url: " + get_url)