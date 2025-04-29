import pytest
from playwright.sync_api import Page, expect

from configs.settings import ACCUWEATHER_URL


@pytest.mark.accuweather
class TestTemperatureUnits:

    def test_temperature_units_change(self, page: Page):
        page.goto(ACCUWEATHER_URL)

        temp_unit_locator = page.locator("span.recent-location-temp-unit")
        temp_unit = "C"
        expect(temp_unit_locator).to_contain_text(temp_unit)
        temp_unit_text = temp_unit_locator.inner_text()
        assert temp_unit_text == temp_unit, f"Expected Celsius (C), but found Fahrenheit (F) instead."

        hamburger_menu_locator = page.locator(".hamburger-button.icon-hamburger")
        hamburger_menu_locator.click()

        settings_locator = page.locator("a:has-text('settings')")
        settings_locator.click()
        expect(page).to_have_url(f"{ACCUWEATHER_URL}/en/settings")
        assert "Settings" in page.title(), "The settings page is not opened"

        unit_selector = page.locator('select#unit.settings-card_setting_select')
        unit_selector.click()

        fahrenheit_locator = page.locator(
            'div.settings-card__setting:has(h2.settings-card__setting__label:text("Units")) ')
        # 'select.settings-card__setting__select')
        desired_unit = "F"
        fahrenheit_locator.select_option(desired_unit)

        page.go_back()
        temp_unit_text = temp_unit_locator.inner_text()
        assert temp_unit_text == desired_unit, f"Expected Fahrenheit (F) as unit, but found Celsius (C) instead"
