from pathlib import Path

import pytest

from configs.settings import TEST_APP_URL
from framework.constants.MainPageNavigation import MainPageNavigation
from framework.ui.browser.browser import Browser
from framework.ui.pages.file_upload_page import FileUploadPage
from framework.ui.pages.main_page import MainPage


@pytest.mark.file_upload
class TestFileUpload:
    def test_file_upload(self, browser: Browser, file_for_upload: Path):
        browser.open_url(TEST_APP_URL)

        main_page = MainPage(browser.page)
        main_page.click_navigation_link(MainPageNavigation.FILE_UPLOAD)

        file_upload_page = FileUploadPage(browser.page)
        file_upload_page.upload_file(file_for_upload)

        uploaded_file_name = file_upload_page.get_uploaded_file_name()
        assert uploaded_file_name == file_for_upload.name, \
            f"Expected uploaded file name to be''{file_for_upload.name}', but got '{uploaded_file_name}'"
