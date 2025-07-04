from playwright.sync_api import Page

from framework.constants import MainPageNavigation
from framework.ui.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, page.locator('h1'), name="Main Page")
        self._navigation_links = page.locator('a')

    def click_navigation_link(self, link_name:MainPageNavigation):
        """Click a navigation link by its visible text
        Args:
            link_name: Enum value from MainPageNavigation
        """
        self._navigation_links.filter(has_text=link_name.value).first.click()
