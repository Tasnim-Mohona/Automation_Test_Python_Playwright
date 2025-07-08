from typing import re

import pytest
from playwright.sync_api import Page

from configs.settings import TEST_APP_URL
from framework.constants.MainPageNavigation import MainPageNavigation
from framework.ui.browser.browser import Browser
from framework.ui.pages.data_tables_page import DataTablesPage
from framework.ui.pages.main_page import MainPage

EXPECTED_DUE_VALUE = 251.00
CURRENCY_SYMBOL = "$"
CURRENCY_REGEX = r"[^\d.]"


@pytest.mark.data_tables
class TestDataTables:

    def test_data_table(self, browser: Browser):
        print("Test Started 🚀")
        browser.open_url(TEST_APP_URL)

        main_page = MainPage(browser.page)
        main_page.click_navigation_link(MainPageNavigation.SORTABLE_DATA_TABLES)

        data_tables_page = DataTablesPage(browser.page)
        table1_content = data_tables_page.get_table1_content()

        total_due = data_tables_page.get_total_due_value(table1_content)
        assert total_due == EXPECTED_DUE_VALUE, \
            f"Expected total due value to be {EXPECTED_DUE_VALUE}, but got {total_due}"
