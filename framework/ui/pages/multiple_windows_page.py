import logging

from playwright.async_api import Page

from framework.ui.elements.button import Button
from framework.ui.pages.base_page import BasePage

logger = logging.getLogger(__name__)


class WindowHandlePage(BasePage):

    def __init__(self, page: Page):
        header_locator = page.locator('a[href="/windows"]')
        super().__init__(page, header_locator, name="Window Handle Page")
        self._click_here_link = Button(page, page.locator('text=click Here'), name="Click Here Link")

    def open_and_switch_to_new_tab(self):
        logger.info("Switching to a New Window")
        return self.click_and_switch_to_new_tab(self._click_here_link)
