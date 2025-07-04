import pytest

from configs.settings import TEST_APP_URL
from framework.constants.MainPageNavigation import MainPageNavigation
from framework.ui.browser.browser import Browser
from framework.ui.pages.checkboxes_page import CheckboxesPage
from framework.ui.pages.main_page import MainPage


@pytest.mark.alerts
class TestCheckboxes:

    def test_checkboxes(self, browser: Browser):
        browser.open_url(TEST_APP_URL)
        main_page = MainPage(browser.page)
        main_page.click_navigation_link(MainPageNavigation.CHECKBOX)
        checkboxes_page = CheckboxesPage(browser.page)

        checkboxes_page.click_checkbox_button()
        assert checkboxes_page.is_page_open(), "Checkboxes page is not open"
