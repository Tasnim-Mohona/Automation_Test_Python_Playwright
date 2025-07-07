from playwright.sync_api import Page

from framework.ui.elements.button import Button
from framework.ui.pages.base_page import BasePage


class ElementsListPage(BasePage):
    def __init__(self, page: Page):
        header_locator = page.locator('h1:has-text("Welcome to the-internet")')
        super().__init__(page, header_locator, name="Elements List Page")
        self.links = Button(page, page.locator('a'), name="Links")

        self.links = page.locator('#content ul a')  # More specific selector

    def count_elements(self) -> int:
        count = self.links.count()
        for i in range(count):
            # href = self.links.nth(i).get_attribute("href")
            text = self.links.nth(i).inner_text()
            # print(f"Link {i + 1}: {href}")
            print(f"Link {i + 1}: {text}")
        return count

    def click_first_link(self) -> str:
        count = self.links.count()
        for i in range(count):
            text = self.links.nth(0).inner_text()
            self.links.nth(0).click()
            print("Clicked the first button.")
            print(f"First Element : {text}")
            return text

            # def count_elements(self) -> int:
            #     count = self.links.count()
            #     for i in range(count):
            #         href = self.links.nth(i).get_attribute("href")
            #         text = self.links.nth(i).inner_text()
            #         print(f"Link {i + 1}: {href}")
            #         self.links.nth(0).click()
            #         print("Clicked the first button.")
            #     return count
