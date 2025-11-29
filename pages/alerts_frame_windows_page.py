from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AlertsFrameWindowsPage(BasePage):

    ALERTS_MENU = (By.ID, "item-1")
    BROWSER_WINDOWS = (By.ID, "item-0")

    def open_alerts(self):
        self.click(self.ALERTS_MENU)

    def open_browser_windows(self):
        self.click(self.BROWSER_WINDOWS)
