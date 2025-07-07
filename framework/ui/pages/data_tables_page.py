from typing import List, Dict

from playwright.sync_api import Page

from framework.ui.decorators.decorators import step
from framework.ui.elements.table import Table
from framework.ui.pages.base_page import BasePage, logger

CURRENCY_SYMBOL = "$"


class DataTablesPage(BasePage):
    def __init__(self, page: Page):
        self.header_locator = page.locator('h3:has-text("Data Tables")')
        super().__init__(page, self.header_locator, "Data Tables Page")

        self._table_1 = Table(
            page,
            table_locator='table#table1',
            name="Table 1"
        )

    @step("Wait for Table #1 to be visible and parse its content")
    def get_table1_content(self) -> List[Dict[str, str]]:
        self._table_1.state.wait_for_displayed()
        return self._table_1.parse_table_content()

    @step("Calculate the total value in the 'Due' column")
    def get_total_due_value(self, content: List[Dict[str, str]]) -> float:
        total_due = sum(
            float(row['Due'].replace(CURRENCY_SYMBOL, "").strip())
            for row in content
        )
        logger.info(f"Total due amount: {CURRENCY_SYMBOL}{total_due}")
        return total_due
