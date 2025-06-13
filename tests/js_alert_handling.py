import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from framework.ui.constants.MainPageNavigation import MainPageNavigation
from framework.ui.pages.MainPage import MainPage
from framework.ui.pages.js_alerts_page import JavaScriptAlertsPage

SUCCESS_ALERT_MSG = "You successfully clicked an alert"


@pytest.mark.alerts
class TestAlertHandling:
    def test_alerts_handling(self, browser: Browser):
        browser.dialog.register_dialog_handler(browser.dialog.accept)
        browser.open_url(TEST_APP_URL)
        main_page = MainPage(browser.page)
        main_page.click_navigation_link(MainPageNavigation.JAVASCRIPT_ALERT)
        js_alerts_page = JavaScriptAlertsPage(browser.page)
        js_alerts_page.trigger_js_alert()
        message = js_alerts_page.get_result_message()
        assert message == SUCCESS_ALERT_MSG, f"Expected success message '{SUCCESS_ALERT_MSG}', but got '{message}'"
