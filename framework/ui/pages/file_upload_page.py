import logging
import pathlib
from typing import Union

from playwright.sync_api import Page

from framework.ui.decorators.decorators import step
from framework.ui.elements.button import Button
from framework.ui.elements.file_uploader import FileUploader
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage

logger = logging.getLogger(__name__)


class FileUploadPage(BasePage):
    def __init__(self, page: Page):
        header_locator = page.locator('h3:has-text("File Uploader")')
        super().__init__(page, header_locator, name="File Uploader Page")

        self._file_input = FileUploader(page, locator="#file-upload", name="File uploader element")
        self._upload_btn = Button(page, locator="#file-submit", name="Upload button")
        self._uploaded_files_lbl = Label(page, locator="#uploaded-files", name="Upload text panel")

    @step("Upload Files")
    def upload_file(self, file_path: Union[pathlib.Path, str]):
        self._file_input.upload_files(file_path)
        self._upload_btn.click()

    @step("Het uploaded file name")
    def get_uploaded_file_name(self) -> str:
        self._uploaded_files_lbl.state.wait_for_displayed()
        return self._uploaded_files_lbl.get_text()
