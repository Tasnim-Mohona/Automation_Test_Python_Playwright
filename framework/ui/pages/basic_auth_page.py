import logging

from playwright.async_api import Page

from framework.ui.decorators.decorators import step
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage

logger = logging.getLogger(__name__)


class BasicAuthPage(BasePage):
    def __init__(self, page: Page):
        header_locator = page.locator('h3:has-text("Basic Auth")')
        super().__init__(page, header_locator, name="Basic Auth Page")

        self._auth_message = Label(page, locator="#content p", name="Basic Auth Message")

    @step("Got Authorization Message")
    def get_auth_message(self) -> str:
        return self._auth_message.get_text()
