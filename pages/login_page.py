from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    SIGNUP_NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BTN = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    ENTER_ACCOUNT_INFO_HEADER = (By.XPATH, "//b[contains(text(),'Enter Account Information')]")
    GENDER_MR = (By.ID, "id_gender1")
    PASSWORD_INPUT = (By.ID, "password")

    # Dropdown
    DAY_SELECT = (By.ID, "days")
    MONTH_SELECT = (By.ID, "months")
    YEAR_SELECT = (By.ID, "years")

    # Checkbox
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")

    # Address
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    ADDRESS_INPUT = (By.ID, "address1")
    COUNTRY_SELECT = (By.ID, "country")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_INPUT = (By.ID, "mobile_number")

    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    ACCOUNT_CREATED_HEADER = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    DELETE_ACCOUNT_BTN = (By.CSS_SELECTOR, "a[href='/delete_account']")
    ACCOUNT_DELETED_HEADER = (By.CSS_SELECTOR, "h2[data-qa='account-deleted']")

    def perform_signup_initial(self, name, email):
        self.type_text(self.SIGNUP_NAME_INPUT, name)
        self.type_text(self.SIGNUP_EMAIL_INPUT, email)
        self.click(self.SIGNUP_BTN)

    def fill_account_details(self, password, first_name, last_name, address, state, city, zipcode, mobile):
        # Radio button
        self.click(self.GENDER_MR)

        # Password
        self.type_text(self.PASSWORD_INPUT, password)

        # Birthdate
        self.select_dropdown(self.DAY_SELECT, "10")
        self.select_dropdown(self.MONTH_SELECT, "May")
        self.select_dropdown(self.YEAR_SELECT, "1990")

        # Checkbox
        self.click(self.NEWSLETTER_CHECKBOX)

        # Address data
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.ADDRESS_INPUT, address)
        self.select_dropdown(self.COUNTRY_SELECT, "Canada")
        self.type_text(self.STATE_INPUT, state)
        self.type_text(self.CITY_INPUT, city)
        self.type_text(self.ZIPCODE_INPUT, zipcode)
        self.type_text(self.MOBILE_INPUT, mobile)

        # Final
        self.click(self.CREATE_ACCOUNT_BTN)

    def is_account_created_message_visible(self):
        try:
            msg = self.get_element_text(self.ACCOUNT_CREATED_HEADER)
            return msg == "ACCOUNT CREATED!"
        except:
            return False

    def get_password_input_element(self):
        return self.find(self.LOGIN_PASSWORD_INPUT)

    def continue_to_home(self):
        self.click(self.CONTINUE_BTN)

    def delete_account(self):
        self.click(self.DELETE_ACCOUNT_BTN)

    def is_account_deleted_message_visible(self):
        try:
            return self.get_element_text(self.ACCOUNT_DELETED_HEADER) == "ACCOUNT DELETED!"
        except:
            return False