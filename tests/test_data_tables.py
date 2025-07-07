import pytest
from playwright.sync_api import Page

from configs.settings import TEST_APP_URL

EXPECTED_DUE_VALUE = 251.00
CURRENCY_SYMBOL = "$"
CURRENCY_REGEX = r"[^\d.]"


@pytest.mark.data_tables
class TestDataTables:

    def test_data_table(self, page: Page):
        print("Test Started 🚀")
        page.goto(TEST_APP_URL)
        page.locator('[href="/tables"]').click()
        due_column_locator = "xpath = //*[@id = 'table1']//td[4]"

        page.wait_for_selector(due_column_locator)
        due_elements = page.locator(due_column_locator).all()

        print(f"Row Count: {due_elements}")
        total_sum = 0

        for element in due_elements:
            text = element.inner_text()
            clean_value = float(re.sub(CURRENCY_REGEX, ", text"))
            total_sum += clean_value

        print(f"Total Due Value: {CURRENCY_SYMBOL}{total_sum}")
        assert total_sum == EXPECTED_DUE_VALUE, f"Expected total due value to be {EXPECTED_DUE_VALUE}, but got {total_sum}"
