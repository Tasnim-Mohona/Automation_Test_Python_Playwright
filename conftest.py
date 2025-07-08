import logging
from enum import Enum
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from configs.settings import DEFAULT_CONFIGURATION_FILE
from framework.logger import logger
from framework.ui.browser.browser import Browser
from framework.ui.browser.window import DEFAULT_VIEWPORT_SIZE
from framework.ui.constants.timeouts import WaitTimeoutsMs

PROJECT_ROOT_DIR = Path(__file__).parent.resolve()


class BrowserType(Enum):
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    WEBKIT = "webkit"


def _get_browser(playwright: sync_playwright, browser_type: BrowserType, headless: bool = False) -> Browser:
    browser_map = {
        BrowserType.FIREFOX: playwright.firefox,
        BrowserType.WEBKIT: playwright.webkit,
        BrowserType.CHROMIUM: playwright.chromium
    }
    browser = browser_map.get(browser_type, playwright.chromium)
    browser_instance = browser.launch(headless=headless)
    context = browser_instance.new_context(viewport=DEFAULT_VIEWPORT_SIZE)
    context.set_default_timeout(WaitTimeoutsMs.WAIT_PAGE_LOAD)

    page = context.new_page()

    custom_browser = Browser(page)
    return custom_browser


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--browser", action="store", default=BrowserType.CHROMIUM.value,
                     help="Choose a browser: chromium, firefox, webkit")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")
    parser.addoption("--config", default=DEFAULT_CONFIGURATION_FILE,
                     help="Path to config file relative to the project root directory")


@pytest.hookimpl(tryfirst=True)
def pytest_configure():
    logger.setup_logger()
    logging.info("Test logging successfully configured for test execution.")


@pytest.fixture(scope="module")
def browser(request):
    browser_channel = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    with sync_playwright() as playwright:
        browser_instance = _get_browser(playwright, BrowserType(browser_channel), headless)
        yield browser_instance

        # Close the browser after the test is done
        browser_instance.page.close()
        browser_instance.page.context.browser.close()
