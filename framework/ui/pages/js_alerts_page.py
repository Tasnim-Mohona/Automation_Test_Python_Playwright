from playwright.sync_api import Page

from framework.ui.decorators.decorators import step
from framework.ui.elements.button import Button
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage


class JavaScriptAlertsPage(BasePage):
    def __init__(self, page: Page):
        header_locator = page.locator('h3:has-text("Javascript Alerts")')
        super().__init__(page, header_locator, name="JavaScript Alerts Page")

        self._js_alert_button = Button(page, page.locator('[onclick *= "jsAlert()"]'), name="Click for JS Alert Button")
        self._result_message_lbl = Label(page, page.locator('#result'), name="Result TextBox")

    @step('Click the JS Alert button')
    def trigger_js_alert(self):
        self._js_alert_button.click()

    @step('Get displayed Result message')
    def get_result_message(self) -> str:
        self._result_message_lbl.state.wait_for_displayed()
        return self._result_message_lbl.get_text()
