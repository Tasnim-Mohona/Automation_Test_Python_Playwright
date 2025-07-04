import logging

from playwright.async_api import Page
from framework.ui.elements.checkbox import Checkbox
from framework.ui.pages.base_page import BasePage

logger = logging.getLogger(__name__)


class CheckboxesPage(BasePage):

    def __init__(self, page: Page):
        header_locator = page.locator('h3:has-text("Checkboxes")')
        super().__init__(page, header_locator, "Checkboxes")

        self._checkbox_button1 = Checkbox(self._page, '#checkboxes input[type="checkbox"]:nth-of-type(1)',
                                          f"Checkbox button 1")
        self._checkbox_button2 = Checkbox(self._page, '#checkboxes input[type="checkbox"]:nth-of-type(2)',
                                          f"Checkbox button 2")

    def click_checkbox_button(self):
        logger.info("Clicking checkbox button")
        self._checkbox_button1.is_checked()
        if self._checkbox_button2.is_checked():
            logger.info("Checkbox button 2 is checked, unchecking it")
            self._checkbox_button2.uncheck()
        self._checkbox_button1.click()
