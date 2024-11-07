from tests.utils import TEST_DATA_DIR, clean_up_files

try:
    from src.assignment.temperature_stats import get_tempreature_stats
except ImportError:
    assert False, "Cannot import get_tempreature_stats from temperature_stats.py"


@clean_up_files
def test_get_tempreature_stats():
    file_path = TEST_DATA_DIR / "test_temperature_stats.txt"
    cities = ["city1", "city2", "city3", "city4", "city5"]
    temperatures = [
        -10.0,
        10.0,
        20.0,
        30.0,
        40.0,
    ]
    with open(file_path, "w") as f:
        for city, temp in zip(cities, temperatures):
            f.write(f"{city},{temp}\n")

    expected_output = {
        "hottest_city": "city5",
        "coldest_city": "city1",
        "average_temperature": 18,
        "temperature_range": 50,
    }

    resutls = get_tempreature_stats(file_path)

    for key in expected_output:
        assert (
            key in resutls
        ), f"expected {key} in output but got {list(resutls.keys())}"

    assert (
        resutls["hottest_city"] == expected_output["hottest_city"]
    ), f"[Hottest City] expected {expected_output['hottest_city']} but got {resutls['hottest_city']}"
    assert (
        resutls["coldest_city"] == expected_output["coldest_city"]
    ), f"[Coldest City] expected {expected_output['coldest_city']} but got {resutls['coldest_city']}"
    assert (
        resutls["average_temperature"] == expected_output["average_temperature"]
    ), f"[Average Temperature] expected {expected_output['average_temperature']} but got {resutls['average_temperature']}"
    assert (
        resutls["temperature_range"] == expected_output["temperature_range"]
    ), f"[Temperature Range] expected {expected_output['temperature_range']} but got {resutls['temperature_range']}"
