import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from framework.ui.constants.MainPageNavigation import MainPageNavigation
from framework.ui.pages.add_remove_page import AddRemovePage
from framework.ui.pages.main_page import MainPage

SUCCESS_ALERT_MSG = "You successfully clicked an alert"


@pytest.mark.alerts
class TestAddRemoveElements:

    def test_add_remove_elements(self, browser: Browser):
        browser.open_url(TEST_APP_URL)

        main_page = MainPage(browser.page)
        main_page.click_navigation_link(MainPageNavigation.Add_REMOVE_ELEMENTS_PAGE)
        add_remove_page = AddRemovePage(browser.page)
        add_remove_page.click_add_element_button()

        add_remove_page.count_remove_elements()
        assert add_remove_page.count_remove_elements() == 1, "Element was not added"
        add_remove_page.click_remove_element_button()
