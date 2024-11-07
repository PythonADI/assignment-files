import random
from typing import Callable
from pathlib import Path

try:
    from src.assignment.data_processing import save_users
except ImportError:
    assert False, "Cannot import save_users from data_processing.py"

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


@clean_up_files
def test_one_user() -> None:
    file_path: Path = TEST_DATA_DIR / "one_user.txt"
    save_users([{"name": "Alice", "age": 25}], file_path.as_posix())

    with file_path.open() as file:
        lines = file.readlines()
        assert (
            len(lines) == 1
        ), f"Function received 1 user, but saved {len(lines)} users"
        assert (
            lines[0].strip() == "Alice,25"
        ), f"Please check the format of the saved user. Expected 'Alice,25', got {lines[0].strip()}"


@clean_up_files
def test_multiple_users() -> None:
    file_path: Path = TEST_DATA_DIR / "multiple_users.txt"
    users = [
        {"name": f"User_{i}", "age": random.randint(18, 65)}
        for i in range(random.randint(5, 100))
    ]

    save_users(users, file_path.as_posix())

    with file_path.open() as file:
        lines = file.readlines()
        assert len(lines) == len(
            users
        ), f"Function received {len(users)} users, but saved {len(lines)} users"

        for i, user in enumerate(users):
            assert (
                lines[i].strip() == f"{user['name']},{user['age']}"
            ), f"Please check the format of the saved user. Expected '{user['name']},{user['age']}', got {lines[i].strip()}"


@clean_up_files
def test_no_users() -> None:
    file_path: Path = TEST_DATA_DIR / "no_users.txt"
    save_users([], file_path.as_posix())

    with file_path.open() as file:
        lines = file.readlines()
        assert (
            len(lines) == 0
        ), f"Function received 0 users, but saved {len(lines)} users"
