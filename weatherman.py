import argparse
from collections import defaultdict
import csv
import os

from utils import clean_csv_lines, print_annual_weather_report, print_hottest_days

USAGE_TEXT = """\
weatherman [report#] [data_dir]

[Report #]
1 for Annual Max/Min Temperature
2 for Hottest day of each year

[data_dir]
Directory containing weather data files
"""


def annual_max_min_temp(data_dir):
    # defaultdict is a subclass of built-in dict.
    # When you try to access a key that doesn’t exist,
    # instead of raising KeyError, it creates a default
    # value automatically.
    yearly_data = defaultdict(
        lambda: {"max_temp": [], "min_temp": [], "max_humidity": [], "min_humidity": []}
    )

    for file_name in os.listdir(data_dir):
        if not file_name.lower().endswith(".txt"):
            continue

        file_path = os.path.join(data_dir, file_name)

        with open(file_path, encoding="utf-8") as file:
            reader = csv.DictReader(clean_csv_lines(file))

            for row in reader:
                date = row.get("PKT")

                if not date:
                    continue

                max_temp = row.get("Max TemperatureC")
                min_temp = row.get("Min TemperatureC")
                max_humidity = row.get("Max Humidity")
                min_humidity = row.get("Min Humidity")

                year = date.split("-")[0]
                if max_temp:
                    yearly_data[year]["max_temp"].append(int(max_temp))
                if min_temp:
                    yearly_data[year]["min_temp"].append(int(min_temp))
                if max_humidity:
                    yearly_data[year]["max_humidity"].append(int(max_humidity))
                if min_humidity:
                    yearly_data[year]["min_humidity"].append(int(min_humidity))

    annual_stats = {}
    for year, data in yearly_data.items():
        # ternary operator syntax `value_if_true if condition else value_if_false`
        max_temp = max(data["max_temp"]) if data["max_temp"] else None
        min_temp = min(data["min_temp"]) if data["min_temp"] else None
        max_humidity = max(data["max_humidity"]) if data["max_humidity"] else None
        min_humidity = min(data["min_humidity"]) if data["min_humidity"] else None

        annual_stats[year] = {
            "max_temp": max_temp,
            "min_temp": min_temp,
            "max_humidity": max_humidity,
            "min_humidity": min_humidity,
        }
    return annual_stats


def hottest_day_each_year(data_dir):
    """
    Returns a dict of hottest day per year
    Format: year -> {"date": "DD/MM/YYYY", "max_temp": value}
    """
    hottest_days = defaultdict(lambda: {"date": None, "max_temp": None})

    for file_name in os.listdir(data_dir):
        if not file_name.lower().endswith(".txt"):
            continue

        file_path = os.path.join(data_dir, file_name)

        with open(file_path, encoding="utf-8") as file:
            reader = csv.DictReader(clean_csv_lines(file))
            for row in reader:
                date = row.get("PKT")
                temp = row.get("Max TemperatureC")
                if not date or not temp:
                    continue

                temp = int(temp)
                year, month, day = date.split("-")
                day = int(day)
                month = int(month)

                # Format date as DD/MM/YYYY
                formatted_date = f"{day}/{month}/{year}"

                # Update hottest day if this temp is higher
                if (
                    hottest_days[year]["max_temp"] is None
                    or temp > hottest_days[year]["max_temp"]
                ):
                    hottest_days[year]["max_temp"] = temp
                    hottest_days[year]["date"] = formatted_date

    return hottest_days


def main():
    parser = argparse.ArgumentParser(
        prog="weatherman",
        usage=USAGE_TEXT,
        description="weatherman [report#] [data_dir]",
    )

    parser.add_argument("report", choices=["1", "2"], help="Report number")

    parser.add_argument("data_dir", help="Directory containing weather data files")

    args = parser.parse_args()

    print("Report:", args.report)
    print("Data dir:", args.data_dir)
    match int(args.report):
        case 1:
            annual_data = annual_max_min_temp(args.data_dir)
            print(annual_data)
            print_annual_weather_report(annual_data)

        case 2:
            hottest_days = hottest_day_each_year(args.data_dir)
            print_hottest_days(hottest_days)


if __name__ == "__main__":
    main()
