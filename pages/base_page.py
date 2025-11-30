import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/"

    def open(self):
        self.driver.get(self.url)
        self.handle_cookie_banner()

    def handle_cookie_banner(self):
        possible_locators = [
            (By.CLASS_NAME, "fc-primary-button"),
            (By.XPATH, "//button[contains(., 'Zgadzam się')]"),
            (By.XPATH, "//p[contains(text(), 'Zgadzam się')]")
        ]

        for locator in possible_locators:
            try:
                wait = WebDriverWait(self.driver, 3)
                button = wait.until(EC.element_to_be_clickable(locator))
                button.click()
                print(" -> Banner closed")
                break
            except TimeoutException:
                pass

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)

    def click(self, locator):
        element = self.find(locator)
        self.scroll_to_element(element)
        element.click()

    def type_text(self, locator, text):
        element = self.find(locator)
        self.scroll_to_element(element)
        element.click()
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title

    def select_dropdown(self, locator, visible_text):
        element = self.find(locator)
        self.scroll_to_element(element)
        select = Select(element)
        select.select_by_visible_text(visible_text)

    def get_element_text(self, locator):
        element = self.find(locator)
        self.scroll_to_element(element)
        return element.text