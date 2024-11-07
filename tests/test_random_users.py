import re
import random
from pathlib import Path
from tests.utils import TEST_DATA_DIR, clean_up_files

try:
    from src.assignment.random_users import generate_random_users, NAME_CHOICES
except ImportError:
    assert (
        False
    ), "Cannot import generate_random_users or NAME_CHOICES from random_users.py"


@clean_up_files
def test_no_users() -> None:
    file_path: Path = TEST_DATA_DIR / "no_users.txt"
    generate_random_users(0, file_path.as_posix())

    assert file_path.exists(), f"File '{file_path.name}' was not created"

    with file_path.open() as file:
        lines = file.readlines()
        assert len(lines) == 0, f"Expected 0 users, got {len(lines)}"


@clean_up_files
def test_one_user() -> None:
    file_path: Path = TEST_DATA_DIR / "one_user.txt"
    generate_random_users(1, file_path.as_posix())

    assert file_path.exists(), f"File '{file_path.name}' was not created"

    with file_path.open() as file:
        lines = file.readlines()
        assert len(lines) == 1, f"Expected 1 user, got {len(lines)}"
        for line in lines:
            assert re.match(
                r"^[A-Z][a-z]+,\d+$", line.strip()
            ), f"Unexpected format: {line.strip()}. Expected 'Name,Age'"
            name, age = line.strip().split(",")
            assert name in NAME_CHOICES, f"Unexpected name: {name}"
            assert (
                18 <= int(age) <= 65
            ), f"Unexpected age: {age}, Expected age between 18 and 65"


@clean_up_files
def test_multiple_users() -> None:
    file_path: Path = TEST_DATA_DIR / "multiple_users.txt"
    n = random.randint(500, 1000)
    generate_random_users(n, file_path.as_posix())

    assert file_path.exists(), f"File '{file_path.name}' was not created"

    with file_path.open() as file:
        lines = file.readlines()
        assert len(lines) == n, f"Expected {n} users, got {len(lines)}"
        for line in lines:
            assert re.match(
                r"^[A-Z][a-z]+,\d+$", line.strip()
            ), f"Unexpected format: {line.strip()}. Expected 'Name,Age'"
            name, age = line.strip().split(",")
            assert name in NAME_CHOICES, f"Unexpected name: {name}"
            assert (
                18 <= int(age) <= 65
            ), f"Unexpected age: {age}, Age should be between 18 and 65"


@clean_up_files
def test_multiple_writes() -> None:
    file_path: Path = TEST_DATA_DIR / "multiple_users.txt"
    n = random.randint(500, 1000)
    generate_random_users(n, file_path.as_posix())
    n_2 = random.randint(500, 1000)
    generate_random_users(n_2, file_path.as_posix())
    n += n_2
    assert file_path.exists(), f"File '{file_path.name}' was not created"

    with file_path.open() as file:
        lines = file.readlines()
        assert (
            len(lines) == n
        ), f"Expected {n} users, got {len(lines)}, Make sure you are appending to the file"
        for line in lines:
            assert re.match(
                r"^[A-Z][a-z]+,\d+$", line.strip()
            ), f"Unexpected format: {line.strip()}. Expected 'Name,Age'"
            name, age = line.strip().split(",")
            assert name in NAME_CHOICES, f"Unexpected name: {name}"
            assert (
                18 <= int(age) <= 65
            ), f"Unexpected age: {age}, Age should be between 18 and 65"
