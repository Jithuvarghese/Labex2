
weather_data = [
    {"date": "2024-07-10", "max_temp": 29, "min_temp": 21, "humidity": 65},
    {"date": "2024-07-11", "max_temp": 30, "min_temp": 22, "humidity": 60},
    {"date": "2024-07-12", "max_temp": 33, "min_temp": 24, "humidity": 70},
    {"date": "2024-07-13", "max_temp": 31, "min_temp": 23, "humidity": 68},
    {"date": "2024-07-14", "max_temp": 35, "min_temp": 25, "humidity": 72},
    {"date": "2024-07-15", "max_temp": 34, "min_temp": 24, "humidity": 66},
    {"date": "2024-07-16", "max_temp": 32, "min_temp": 22, "humidity": 64},
    {"date": "2024-07-17", "max_temp": 28, "min_temp": 20, "humidity": 62},
    {"date": "2024-07-18", "max_temp": 30, "min_temp": 22, "humidity": 63},
    {"date": "2024-07-19", "max_temp": 31, "min_temp": 23, "humidity": 65},
    {"date": "2024-07-20", "max_temp": 29, "min_temp": 21, "humidity": 60},
    {"date": "2024-07-21", "max_temp": 33, "min_temp": 24, "humidity": 68},
    {"date": "2024-07-22", "max_temp": 30, "min_temp": 22, "humidity": 67},
    {"date": "2024-07-23", "max_temp": 32, "min_temp": 23, "humidity": 69},
    {"date": "2024-07-24", "max_temp": 28, "min_temp": 20, "humidity": 64},
    {"date": "2024-07-25", "max_temp": 29, "min_temp": 21, "humidity": 61},
    {"date": "2024-07-26", "max_temp": 30, "min_temp": 22, "humidity": 65},
    {"date": "2024-07-27", "max_temp": 32, "min_temp": 23, "humidity": 66},
    {"date": "2024-07-28", "max_temp": 34, "min_temp": 24, "humidity": 70},
    {"date": "2024-07-29", "max_temp": 31, "min_temp": 23, "humidity": 68},
    {"date": "2024-07-30", "max_temp": 30, "min_temp": 22, "humidity": 65},
    {"date": "2024-07-31", "max_temp": 33, "min_temp": 24, "humidity": 72},
    {"date": "2024-08-01", "max_temp": 34, "min_temp": 25, "humidity": 70},
]

def find_highest_and_lowest_temps(weather_data):
    highest_temp = float('-inf')
    lowest_temp = float('inf')
    for day_data in weather_data:
        highest_temp = max(highest_temp, day_data["max_temp"])
        lowest_temp = min(lowest_temp, day_data["min_temp"])
    return highest_temp, lowest_temp


def count_days_above_30(weather_data):
    count = 0
    for day_data in weather_data:
        if day_data["max_temp"] > 30:
            count += 1
    return count

def average_humidity(weather_data):
    total_humidity = 0
    for day_data in weather_data:
        total_humidity += day_data["humidity"]
    return total_humidity / len(weather_data)

highest_temp, lowest_temp = find_highest_and_lowest_temps(weather_data)
days_above_30 = count_days_above_30(weather_data)
avg_humidity = average_humidity(weather_data)

print(f"Highest temperature: {highest_temp}°C")
print(f"Lowest temperature: {lowest_temp}°C")
print(f"Days with temperature above 30°C: {days_above_30}")
print(f"Average humidity: {avg_humidity:.2f}%")
