from playwright.async_api import Page

from framework.ui.pages.base_page import BasePage


class NewWindowPage(BasePage):

    def __init__(self, page: Page):
        header_locator = page.locator('h3:has-text("New Window")')
        super().__init__(page, header_locator, name="New Window Page")
