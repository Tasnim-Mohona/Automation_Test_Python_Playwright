from playwright.sync_api import Page

from framework.ui.pages.base_page import BasePage


class AbTestPage(BasePage):

    def __init__(self, page: Page):
        self.header_locator = page.locator("h3:has-text('A/B Test')")
        super().__init__(page, self.header_locator, name="A/B test")

    def get_header_text(self) -> str:
        text = self.header_locator.inner_text()
        print(f"Header text: {text}")
        return text
