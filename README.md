# Working with files

### Careful
- note before submitting every file should only contain function definitions, no print statements or input statements, nor function calls at global scope.
- if you still want to use your functions read [about guard clause and main function](https://realpython.com/python-main-function/)


1. complete function in [data_processsing.py](./src/assignment/data_processing.py). It should receive a `users` (list) `file_path` (string) and it should save each user on separate lines in the file.

---

Example how this function is used:

input:
```python
users = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Doe", "age": 35}
]

file_path = "users.txt"

save_users(users, file_path)
```

output (users.txt):
```
John,30
Jane,25
Doe,35
```

---

2. In [random_users.py](./src/assignment/random_users.py) complete function `generate_random_users` that receives a number `n` and saves users to a file (file should be appended with the new users), each user should be on a separate line. Each user should be on a separate line and should have the following format: `name,age`. The `name` should be a random string from `NAME_CHOICES` list and the `age` should be a random integer between 18 and 65.

HINT: to get random name from the `NAME_CHOICES` list. You can use the `random.choice` function from the `random` module.

---

Example how this function is used:

input:
```python
n = 3

users = generate_random_users(n, "random_users.txt")
```

output (random_users.txt):
```
John,30
Jane,25
Doe,35
```

---

3. You are given a file of example of temperatures in [temperatures.txt](./src/assignment/temperatures.txt) (THIS IS JUST AN EXAMPLE FILE TO TEST YOURSELF). Each line in the file contains a city name and a temperature separated by a comma. Complete function `get_temperature_stats` in [temperature_stats.py](./src/assignment/temperature_stats.py) that reads the file and returns a dictionary with the following keys:
    - `hottest_city` - the city with the highest temperature
    - `coldest_city` - the city with the lowest temperature
    - `average_temperature` - the average temperature of all cities
    - `temperature_range` - the difference between the highest and lowest temperature

NOTE: in test cases temperatures files will differ, so you should not hardcode the expected values.

---

Example how this function is used:

input:
```python
file_path = "temperatures.txt"

stats = get_temperature_stats(file_path)
print(stats)
```

temperature.txt:
```
Lisbon,20
Moscow,-10
Paris,15
```

output (return value of `get_temperature_stats`):
```python
{
    "hottest_city": "Lisbon",
    "coldest_city": "Moscow",
    "average_temperature": 15.0,
    "temperature_range": 30
}
```

---

4. Now we got more data about temperatures, each city might have more than one temperature, we don't know how many **BUT** there will be at least one temperature for each city. Example is given in [temperatures_v2.txt](./src/assignment/temperatures_v2.txt) file (THIS IS JUST AN EXAMPLE FILE TO TEST YOURSELF).
Complete function `get_temperature_stats_v2` in [temperature_stats_v2.py](./src/assignment/temperature_stats_v2.py) that reads the file and returns a dictionary with the following keys:
    - `hottest_city` - the city with the highest average temperature
    - `coldest_city` - the city with the lowest average temperature
    - `average_temperature` - the average temperature of all cities
    - `temperature_range` - the difference between the highest and lowest average temperature

NOTE: in test cases temperatures files will differ, so you should not hardcode the expected values.
HINT: use dictionary and list to store the temperatures for each city.

---

Example how this function is used:

input:
```python
file_path = "temperatures_v2.txt"

stats = get_temperature_stats_v2(file_path)
print(stats)
```

temperature.txt:
```
Lisbon,20
Moscow,-10
Moscow,-13
Paris,15
Paris,20
Paris,10
```

output (return value of `get_temperature_stats_v2`):
```python
{
    "hottest_city": "Paris",
    "coldest_city": "Moscow",
    "average_temperature": 10.33,
    "temperature_range": 30
}
```


