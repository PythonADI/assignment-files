import random
from tests.utils import TEST_DATA_DIR, clean_up_files

try:
    from src.assignment.temperature_stats_v2 import get_temperature_stats_v2
except ImportError:
    assert False, "Cannot import get_tempreature_stats from temperature_stats.py"


@clean_up_files
def test_get_tempreature_stats():
    file_path = TEST_DATA_DIR / "test_temperature_stats.txt"
    cities = ["city1", "city2", "city3", "city4", "city5"]
    cities_data = [
        {random.choice(cities): random.uniform(-100, 100)} for _ in range(1000)
    ]

    temps = {}
    for city_data in cities_data:
        for city, temp in city_data.items():
            temps[city] = temps.get(city, 0) + temp

    with open(file_path, "w") as f:
        for city, temp in temps.items():
            f.write(f"{city},{temp}\n")

    expected_output = {
        "hottest_city": max(temps, key=temps.get),
        "coldest_city": min(temps, key=temps.get),
        "average_temperature": sum(temps.values()) / len(temps),
        "temperature_range": max(temps.values()) - min(temps.values()),
    }

    resutls = get_temperature_stats_v2(file_path)

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
