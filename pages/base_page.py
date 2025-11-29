from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ============================
    # CORE ELEMENT ACTIONS
    # ============================

    def wait_for_visible(self, locator):
        """Wait until element is visible"""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element not visible: {locator}")

    def wait_for_clickable(self, locator):
        """Wait until element is clickable"""
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise Exception(f"Element not clickable: {locator}")

    def click(self, locator):
        """Click element"""
        element = self.wait_for_clickable(locator)
        element.click()

    def type(self, locator, text, clear_first=True):
        """Type text in input box"""
        element = self.wait_for_visible(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get visible text"""
        element = self.wait_for_visible(locator)
        return element.text

    def is_element_present(self, locator):
        """Check if element exists (no wait)"""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def get_title(self):
        """Get current page title"""
        return self.driver.title

    # ============================
    # EXTRA UTILITIES
    # ============================

    def scroll_to(self, locator):
        """Scroll to element"""
        element = self.wait_for_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_for_url(self, text):
        """Wait until URL contains given text"""
        try:
            self.wait.until(EC.url_contains(text))
        except TimeoutException:
            raise Exception(f"URL does not contain expected text: {text}")
