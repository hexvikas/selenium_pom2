import pytest
from utils.driver_factory import get_driver
from utils.read_config import read_testdata
from pages.home_page import HomePage
from pages.elements_page import ElementsPage
from pages.textbox_page import TextBoxPage


def test_textbox_form():
    driver = get_driver()
    data = read_testdata()

    driver.get(data["url"])

    home = HomePage(driver)
    home.click_elements()

    elements = ElementsPage(driver)
    elements.open_textbox()

    text = TextBoxPage(driver)
    text.fill_textbox_form(
        name=data["username"],
        email=data["email"],
        current=data["currentAddress"],
        permanent=data["permanentAddress"]
    )

    assert data["username"] in text.get_output_name()
    assert data["email"] in text.get_output_email()

    driver.quit()
