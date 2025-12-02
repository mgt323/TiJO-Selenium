import pytest
import time
import random
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def generate_email():
    return f"testuser_{random.randint(1000, 9999)}@test.com"


class TestFunctional:

    # FT01: Registration
    def test_ft01_registration(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open()
        main_page.go_to_login()

        unique_email = generate_email()
        login_page.perform_signup_initial("Jan Kowalski", unique_email)

        login_page.fill_account_details(
            password="StrongPassword123!",
            first_name="Jan",
            last_name="Kowalski",
            address="Ulica Testowa 123",
            state="Dolnoslaskie",
            city="Wroclaw",
            zipcode="00-001",
            mobile="123456789"
        )

        assert login_page.is_account_created_message_visible() is True, "'ACCOUNT CREATED!' is not visible"

        login_page.continue_to_home()
        login_page.delete_account()

        assert login_page.is_account_deleted_message_visible() is True, "Couldn't delete account (Cleanup failed)"

    # FT04: Product Class Search
    def test_ft04_search_product(self, driver):
        main_page = MainPage(driver)
        product_page = ProductPage(driver)

        main_page.open()
        main_page.go_to_products()

        search_term = "Dress"
        product_page.search_product(search_term)

        assert product_page.get_searched_products_count() > 0, "No searched products found"

    # FT07: Product Quantity Change
    @pytest.mark.parametrize("quantity_input, expected_quantity", [
        ("1", "1"),
        ("0", "1"),
        ("-1", "1")
    ])
    def test_ft07_product_quantity_bva(self, driver, quantity_input, expected_quantity):
        main_page = MainPage(driver)
        product_page = ProductPage(driver)

        main_page.open()

        product_page.view_first_product()
        product_page.change_quantity(quantity_input)

        product_page.add_to_cart()
        product_page.go_to_cart()

        actual_quantity = product_page.get_cart_quantity()
        assert actual_quantity == expected_quantity, \
            f"ERROR! For input '{quantity_input}', '{actual_quantity}' was found in cart, expecting '{expected_quantity}'."