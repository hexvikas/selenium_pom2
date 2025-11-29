from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TextBoxPage(BasePage):

    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT_BTN = (By.ID, "submit")

    OUTPUT_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")

    def fill_textbox_form(self, name, email, current, permanent):
        self.type(self.FULL_NAME, name)
        self.type(self.EMAIL, email)
        self.type(self.CURRENT_ADDRESS, current)
        self.type(self.PERMANENT_ADDRESS, permanent)
        self.click(self.SUBMIT_BTN)

    def get_output_name(self):
        return self.get_text(self.OUTPUT_NAME)

    def get_output_email(self):
        return self.get_text(self.OUTPUT_EMAIL)
