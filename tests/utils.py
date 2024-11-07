from typing import Callable
from pathlib import Path

TEST_DATA_DIR = Path(__file__).parent / "data"
DATA_DIR = Path(__file__).parent.parent / "src" / "assignment" / "data"


def clean_up_files(func: Callable[[], None]) -> None:
    def wrapper() -> None:
        try:
            TEST_DATA_DIR.mkdir(exist_ok=True)
            func()
        finally:
            if TEST_DATA_DIR.exists():
                for file in TEST_DATA_DIR.iterdir():
                    file.unlink()
                TEST_DATA_DIR.rmdir()

    return wrapper
