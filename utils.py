def clean_csv_lines(file_obj):
    """
    Yield only valid CSV lines, skipping HTML/footer lines.
    """
    for line in file_obj:
        line = line.strip()
        if not line or line.startswith("<"):
            continue
        yield line


def print_annual_weather_report(annual_data):
    print(
        "Year  MAX Temp  MIN Temp  MAX Humidity  MIN Humidity"
    )
    print("-" * 74)

    for year in sorted(annual_data):
        data = annual_data[year]
        print(
            f"{year:<5} "
            f"{data['max_temp']:<9} "
            f"{data['min_temp']:<9} "
            f"{data['max_humidity']:<13} "
            f"{data['min_humidity']}"
        )


def print_hottest_days(hottest_days):
    print("Year Date        Temp")
    print("-" * 30)
    for year in sorted(hottest_days):
        data = hottest_days[year]
        print(f"{year} {data['date']:<12} {data['max_temp']}")
