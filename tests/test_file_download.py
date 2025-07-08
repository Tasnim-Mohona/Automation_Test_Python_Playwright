from pathlib import Path

import pytest

from configs.settings import TEST_APP_URL
from framework.constants.MainPageNavigation import MainPageNavigation
from framework.ui.browser.browser import Browser
from framework.ui.pages.file_download_page import FileDownloadPage
from framework.ui.pages.main_page import MainPage


@pytest.mark.file_download
@pytest.mark.userfixtures("cleanup_download_dir")
class TestFileDownload:
    def test_file_download(self, browser: Browser, test_file_name: str, download_dir: Path):
        browser.open_url(TEST_APP_URL)
        main_page = MainPage(browser.page)
        main_page.click_navigation_link(MainPageNavigation.FILE_DOWNLOAD)

        file_download_page = FileDownloadPage(browser.page)
        assert file_download_page.is_file_enabled(test_file_name),\
            f"Downloaded file was not found at '{downloaded_file_path}'"





