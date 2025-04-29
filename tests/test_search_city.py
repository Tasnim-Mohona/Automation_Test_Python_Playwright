import pytest
from playwright.async_api import expect, Page

from configs.settings import ACCUWEATHER_URL


@pytest.mark.accuweather
class TestAccuWeatherSearch:
    def test_search_city(self, page: Page):
        page.goto(ACCUWEATHER_URL, wait_until="domcontentloaded")

        consent_button_locator = page.locator(".banner-button")

        if consent_button_locator.is_visible():
            consent_button_locator.click()

        city_name = "New York"
        search_input = page.locator(".search-input")
        search_input.click()
        page.keyboard.type(city_name)

        results_container = page.locator("div.results-container")
        results_container.wait_for(state="visible")
        assert results_container.is_visible(), "Results container is not visible"
        expect(results_container).to_be_visible(timeout=10000)

        first_result = page.locator("div.search-result >> nth = 0")
        first_result.click()

        city_page_locator = page.locator("h1.header-loc")
        city_page_locator.wait_for(state = "visible")

        assert city_page_locator.is_visible(), "City header is not visible on the page."
        text = city_page_locator.inner_text()

        assert city_name in text, f"expected '{city_name}' in the test, but gotL '{text}'"
