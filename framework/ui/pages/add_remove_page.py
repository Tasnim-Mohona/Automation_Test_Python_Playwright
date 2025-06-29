import logging

from playwright.sync_api import Page

from framework.ui.elements.button import Button
from framework.ui.pages.base_page import BasePage

logger = logging.getLogger(__name__)


class AddRemovePage(BasePage):

    def __init__(self, page: Page):
        header_locator = page.locator('h3:has-text("Add/RemoveElements")')
        super().__init__(page, header_locator, "Add/Remove Page")

        self._add_button = Button(self._page, '[onclick = "addElement()"]', f"add button")
        self._delete_button = Button(self._page, '[onclick = "deleteElement()"]', f"delete button")

    def click_add_element_button(self):
        logger.info("Clicking 'Add element' button")
        self._add_button.click()

    def click_remove_element_button(self):
        logger.info("Counting 'Remove Element' buttons")
        return self._delete_button.count()

    def count_remove_elements(self):
        logger.info("Counting 'Remove Element' buttons")
        return self._delete_button.count()
