import os
import time
import base64
from pathlib import Path
from typing import Union

UTF8 = "utf-8"


def is_file_exists(file_path: Union[str, Path], timeout_seconds: int = 10) -> bool:
    """
    Wait for a file to exist within the specified timeout period.

    Args:
        file_path: Path to the file as string or Path object
        timeout_seconds: Maximum time to wait in seconds (default: 10)

    Returns:
        bool: True if file exists within timeout, False otherwise
    """
    path = Path(file_path) if isinstance(file_path, str) else file_path
    end_time = time.time() + timeout_seconds

    while time.time() < end_time:
        if path.exists():
            return True
        time.sleep(0.5)  # Check every 0.5 seconds

    return False


def remove_dir_if_exist(file_path: Union[str, Path]) -> None:
    """
    Delete a file if it exists.

    Args:
        file_path: Path to the file as string or Path object
    """
    path = Path(file_path) if isinstance(file_path, str) else file_path
    try:
        if path.exists():
            path.unlink()  # Remove the file
    except OSError as e:
        print(f"Error deleting file {file_path}: {e}")