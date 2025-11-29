from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    # ========== LOCATORS ==========
    USERNAME_INPUT = (By.ID, "userName")           # Change ID based on website
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")

    PROFILE_NAME = (By.ID, "userName-value")       # After login, visible username

    # ========== ACTIONS ==========
    def enter_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # ========== VALIDATION ==========
    def get_logged_in_username(self):
        return self.get_text(self.PROFILE_NAME)
