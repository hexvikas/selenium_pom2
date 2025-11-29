from utils.driver_factory import get_driver
from utils.read_config import read_testdata
from pages.home_page import HomePage
from pages.alerts_frame_windows_page import AlertsFrameWindowsPage
from pages.alerts_page import AlertsPage

def test_alerts():
    driver = get_driver()
    data = read_testdata()

    driver.get(data["url"])

    home = HomePage(driver)
    home.click_alerts_frame_windows()

    alerts_menu = AlertsFrameWindowsPage(driver)
    alerts_menu.open_alerts()

    alerts = AlertsPage(driver)
    alerts.click_simple_alert()

    driver.quit()
