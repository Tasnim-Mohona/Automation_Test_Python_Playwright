import pytest

from configs.settings import TEST_APP_URL
from framework.ui.browser.browser import Browser
from framework.ui.pages.accuweather_main_Page import AccuWeatherMainPage


@pytest.mark.test_accuweather
class TestAccuWeather:
    def test_accuweather(self, browser: Browser):
        browser.open_url(TEST_APP_URL)
        accuweather_main_page = AccuWeatherMainPage(browser.page)
        accuweather_main_page.dismiss_ad_if_present()
        accuweather_main_page.accept_consent_data_usage()
        browser.dialog.accept(dialog="Consent Dialog")
        current_url = browser.get_current_url()
        browser.wait_for_delay()
        browser.window.switch_to_window()
        browser.window.switch_to_first_window()


