from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    # Lokatory
    SIGNUP_LOGIN_BTN = (By.CSS_SELECTOR, "a[href='/login']")
    PRODUCTS_BTN = (By.CSS_SELECTOR, "a[href='/products']")
    LOGO = (By.CSS_SELECTOR, "img[alt='Website for automation practice']")

    # Metody
    def go_to_login(self):
        self.click(self.SIGNUP_LOGIN_BTN)

    def go_to_products(self):
        self.click(self.PRODUCTS_BTN)

    def is_logo_visible(self):
        return self.find(self.LOGO).is_displayed()