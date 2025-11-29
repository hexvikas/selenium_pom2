from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ElementsPage(BasePage):

    TEXTBOX_MENU = (By.ID, "item-0")
    CHECKBOX_MENU = (By.ID, "item-1")
    RADIO_MENU = (By.ID, "item-2")
    BUTTONS_MENU = (By.ID, "item-4")

    def open_textbox(self):
        self.click(self.TEXTBOX_MENU)

    def open_checkbox(self):
        self.click(self.CHECKBOX_MENU)

    def open_radio(self):
        self.click(self.RADIO_MENU)

    def open_buttons(self):
        self.click(self.BUTTONS_MENU)
