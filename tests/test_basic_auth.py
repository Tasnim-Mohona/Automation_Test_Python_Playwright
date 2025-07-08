import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from framework.constants.MainPageNavigation import MainPageNavigation
from framework.ui.pages.main_page import MainPage
from framework.ui.pages.basic_auth_page import BasicAuthPage

SUCCESS_AUTH_MSG = "Congratulations! You must have the proper credentials"


@pytest.mark.basic_auth
@pytest.mark.usefixtures("set_basic_auth")
class TestBasicAuth:
    def test_basic_auth(self, browser: Browser):
        browser.open_url(TEST_APP_URL)

        main_page = MainPage(browser.page)
        main_page.click_navigation_link(MainPageNavigation.BASIC_AUTH)

        basic_auth_page = BasicAuthPage(browser.dialog.page)
        basic_auth_page.wait_for_page_to_load()

        text = basic_auth_page.get_auth_message()
        assert text.startswith(SUCCESS_AUTH_MSG), f"Expected text message '{SUCCESS_AUTH_MSG}', but got '{text}'"
