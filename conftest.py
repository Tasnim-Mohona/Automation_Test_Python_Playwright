import json
import logging
from enum import Enum
from pathlib import Path
from typing import Dict

import pytest
from playwright.sync_api import sync_playwright

from configs.settings import DEFAULT_CONFIGURATION_FILE
from framework.logger import logger
from framework.ui.browser.browser import Browser
from framework.ui.browser.window import DEFAULT_VIEWPORT_SIZE
from framework.ui.constants.timeouts import WaitTimeoutsMs
from framework.utils.config_parser import get_config_value

PROJECT_ROOT_DIR = Path(__file__).parent.resolve()
DEFAULT_TEST_FILE = Path("default_file.txt")
DEFAULT_DOWNLOAD_DIR = Path("/downloads")
DEFAULT_RESOURCE_DIR = Path("resources")


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


@pytest.fixture(scope="module")
def set_basic_auth(browser: Browser, test_config: Dict[str, str]) -> None:
    user = get_config_value(test_config, key="user", required=True)
    password = get_config_value(test_config, key="password", required=True)
    browser.set_basic_authentication(user, password)


@pytest.fixture(scope="session")
def test_config(request) -> dict[str, str]:
    config_file = request.config.getoption("--config")
    config_path = PROJECT_ROOT_DIR.joinpath(config_file).resolve()
    try:
        with open(config_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise Exception(f"Configuration file not found at : {config_path}")
    return data
