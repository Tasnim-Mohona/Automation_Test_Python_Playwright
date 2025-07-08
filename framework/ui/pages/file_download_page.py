import logging
from pathlib import Path

from playwright.sync_api import Page

from framework.ui.decorators.decorators import step
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage

logger = logging.getLogger(__name__)


class FileDownloadPage(BasePage):

    def __init__(self, page: Page):
        header_locator = page.locator('h3:has-text("File Downloader")')
        super().__init__(page, header_locator, name="File Downloader Page")

        self._file_locator_template = '[href="download/{}"]'

    def get_file_link(self, file_name: str) -> Label:
        return Label(
            self.page,
            self._file_locator_template.format(file_name),
            name=f"Download link for '{file_name}'"
        )

    @step("Check if download link for file is displayed")
    def is_file_enabled(self, file_name: str) -> bool:
        file_link = self.get_file_link(file_name)
        return file_link.state.is_enabled()

    @step("Download file")
    def download_file(self, file_name: str, download_dir: Path) -> Path:
        file_link = self.get_file_link(file_name)
        logger.debug(f"Start downloading file '{file_name}'")

        with self.page.expect_download() as download_info:
            file_link.click()
            download = download_info.value

        downloaded_file_path = download_dir.joinpath(file_name)
        download.save_as(downloaded_file_path)

        logger.debug(f"File saved to '{downloaded_file_path}'")
        return downloaded_file_path

