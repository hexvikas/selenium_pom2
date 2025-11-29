from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    ELEMENTS_CARD = (By.XPATH, "//h5[text()='Elements']/ancestor::div[@class='card mt-4 top-card']")
    ALERTS_CARD = (By.XPATH, "//h5[text()='Alerts, Frame & Windows']/ancestor::div[@class='card mt-4 top-card']")
    WIDGETS_CARD = (By.XPATH, "//h5[text()='Widgets']/ancestor::div[@class='card mt-4 top-card']")

    def click_elements(self):
        self.scroll_to(self.ELEMENTS_CARD)
        self.click(self.ELEMENTS_CARD)

    def click_alerts_frame_windows(self):
        self.scroll_to(self.ALERTS_CARD)
        self.click(self.ALERTS_CARD)

    def click_widgets(self):
        self.scroll_to(self.WIDGETS_CARD)
        self.click(self.WIDGETS_CARD)
