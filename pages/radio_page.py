from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RadioPage(BasePage):

    YES_RADIO = (By.XPATH, "//label[@for='yesRadio']")
    IMPRESSIVE_RADIO = (By.XPATH, "//label[@for='impressiveRadio']")
    RESULT_TEXT = (By.CLASS_NAME, "text-success")

    def click_yes(self):
        self.click(self.YES_RADIO)

    def click_impressive(self):
        self.click(self.IMPRESSIVE_RADIO)

    def get_result(self):
        return self.get_text(self.RESULT_TEXT)
