from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AlertsPage(BasePage):

    SIMPLE_ALERT = (By.ID, "alertButton")
    TIMER_ALERT = (By.ID, "timerAlertButton")
    CONFIRM_ALERT = (By.ID, "confirmButton")
    PROMPT_ALERT = (By.ID, "promtButton")

    CONFIRM_RESULT = (By.ID, "confirmResult")
    PROMPT_RESULT = (By.ID, "promptResult")

    def click_simple_alert(self):
        self.click(self.SIMPLE_ALERT)
        self.driver.switch_to.alert.accept()

    def click_confirm_alert(self):
        self.click(self.CONFIRM_ALERT)
        self.driver.switch_to.alert.accept()

    def click_prompt_alert(self, text):
        self.click(self.PROMPT_ALERT)
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def get_confirm_result(self):
        return self.get_text(self.CONFIRM_RESULT)

    def get_prompt_result(self):
        return self.get_text(self.PROMPT_RESULT)
