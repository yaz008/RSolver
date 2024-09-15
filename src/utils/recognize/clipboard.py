import win32clipboard
from contextlib import contextmanager
from typing import Generator

@contextmanager
def clipboard() -> Generator[str, None, None]:
    try:
        win32clipboard.OpenClipboard()  # Open the clipboard
        yield win32clipboard.GetClipboardData()
    finally:
        win32clipboard.CloseClipboard()