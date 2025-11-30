import pytest
import time
from selenium.webdriver.common.keys import Keys
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestNonFunctional:

    # NFT01: Main Page Load Time
    def test_nft01_load_time(self, driver):
        main_page = MainPage(driver)

        start_time = time.time()
        main_page.open()
        main_page.is_logo_visible()
        end_time = time.time()

        load_time = end_time - start_time
        print(f"Czas ładowania: {load_time:.2f}s")

        assert load_time < 4.0, "Website's load time is too low"

    # NFT02: Password masking
    def test_nft02_password_masking(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open()
        main_page.go_to_login()

        pass_input = login_page.get_password_input_element()
        input_type = pass_input.get_attribute("type")

        assert input_type == "password", "Password input is not masked"

    # NFT03: Availability (Tab order)
    def test_nft03_tab_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open()
        main_page.go_to_login()

        email_input = login_page.find(login_page.LOGIN_EMAIL_INPUT)
        email_input.click()

        email_input.send_keys(Keys.TAB)

        active_element = driver.switch_to.active_element
        active_attrib = active_element.get_attribute("data-qa")

        assert active_attrib == "login-password", "Tab order is not correct"