from enum import Enum
from typing import final


@final
class MainPageNavigation(Enum):
    JAVASCRIPT_ALERT = "JavaScript Alerts"
    SORTABLE_DATA_TABLES = "Sortable Data Tables"
    DYNAMIC_CONTROLS = "Dynamic Controls"
    FILE_DOWNLOAD = "File Download"
    FILE_UPLOAD = "File Upload"
    BASIC_AUTH = "Basic Auth"
    Add_REMOVE_ELEMENTS_PAGE = "Add/Remove Elements"
    MULTIPLE_WINDOWS = "Multiple Windows"
    CHECKBOX = "Checkboxes"

    @property
    def label(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.label
