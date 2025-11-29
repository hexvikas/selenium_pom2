from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckBoxPage(BasePage):

    EXPAND_BTN = (By.XPATH, "//button[@title='Expand all']")
    HOME_CHECKBOX = (By.XPATH, "//span[@class='rct-title' and text()='Home']")
    RESULT_TEXT = (By.ID, "result")

    def expand_all(self):
        self.click(self.EXPAND_BTN)

    def select_home(self):
        self.click(self.HOME_CHECKBOX)

    def get_result(self):
        return self.get_text(self.RESULT_TEXT)
