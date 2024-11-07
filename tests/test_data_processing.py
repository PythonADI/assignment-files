import random
from pathlib import Path
from tests.utils import TEST_DATA_DIR, clean_up_files

try:
    from src.assignment.data_processing import save_users
except ImportError:
    assert False, "Cannot import save_users from data_processing.py"


@clean_up_files
def test_one_user() -> None:
    file_path: Path = TEST_DATA_DIR / "one_user.txt"
    save_users([{"name": "Alice", "age": 25}], file_path.as_posix())

    assert file_path.exists(), f"File '{file_path.name}' was not created"

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

    assert file_path.exists(), f"File '{file_path.name}' was not created"

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

    assert file_path.exists(), f"File '{file_path.name}' was not created"

    with file_path.open() as file:
        lines = file.readlines()
        assert (
            len(lines) == 0
        ), f"Function received 0 users, but saved {len(lines)} users"
