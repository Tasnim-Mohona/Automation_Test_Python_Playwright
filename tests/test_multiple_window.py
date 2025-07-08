import pytest

from configs.settings import TEST_APP_URL
from framework.constants.MainPageNavigation import MainPageNavigation
from framework.ui.browser.browser import Browser
from framework.ui.pages.main_page import MainPage
from framework.ui.pages.multiple_windows_page import WindowHandlePage
from framework.ui.pages.new_window_page import NewWindowPage


@pytest.mark.final
class TestMultipleWindow:
    def test_multiple_window(self, browser: Browser):
        browser.open_url(TEST_APP_URL)
        main_page = MainPage(browser.page)
        main_page.click_navigation_link(MainPageNavigation.MULTIPLE_WINDOWS)

        multiple_window_page = WindowHandlePage(browser.page)
        new_window_page = NewWindowPage(browser.page)

        multiple_window_page.open_and_switch_to_new_tab()
        browser.wait_for_delay(500)
        new_window_page.wait_for_page_to_load()
        assert new_window_page.is_page_open(), "New Window Page did not open successfully"
