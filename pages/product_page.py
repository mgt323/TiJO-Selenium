from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    # Lokatory
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BTN = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_HEADER = (By.CSS_SELECTOR, ".features_items h2")
    PRODUCT_LIST = (By.CSS_SELECTOR, ".features_items .col-sm-4")

    VIEW_PRODUCT_BTN = (By.CSS_SELECTOR, "a[href='/product_details/1']")  # Dla pierwszego produktu
    QUANTITY_INPUT = (By.ID, "quantity")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.cart")
    VIEW_CART_LINK = (By.XPATH, "//u[contains(text(),'View Cart')]")
    CART_QUANTITY = (By.CSS_SELECTOR, "button.disabled")  # W koszyku ilość jest często w disabled button

    def search_product(self, text):
        self.type_text(self.SEARCH_INPUT, text)
        self.click(self.SEARCH_BTN)

    def get_searched_products_count(self):
        # Zwraca ilość znalezionych kafelków z produktami
        return len(self.driver.find_elements(*self.PRODUCT_LIST))

    def view_first_product(self):
        self.click(self.VIEW_PRODUCT_BTN)

    def change_quantity(self, qty):
        self.type_text(self.QUANTITY_INPUT, qty)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def go_to_cart(self):
        # Czekamy aż modal się pojawi
        self.click(self.VIEW_CART_LINK)

    def get_cart_quantity(self):
        return self.find(self.CART_QUANTITY).text