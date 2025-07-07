import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from framework.ui.pages.ab_test_page import AbTestPage
from framework.ui.pages.elements_list_page import ElementsListPage


@pytest.mark.alerts
class TestElementList:
    def test_elements_list(self, browser: Browser):
        browser.open_url(TEST_APP_URL)
        elements_list_page = ElementsListPage(browser.page)

        assert elements_list_page.is_page_open(), "Elements list page failed to load"
        total_links = elements_list_page.count_elements()
        print(f"Total links found: {total_links}")
        elements_list_page.click_first_link()
        ab_test_page = AbTestPage(browser.page)
        text = ab_test_page.get_header_text()
        # assert text == elements_list_page.click_first_link(), "The first link didn't open"
        assert ab_test_page.is_page_open(), "First Link didn't open"
