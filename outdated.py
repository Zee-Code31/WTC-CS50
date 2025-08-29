def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        date_str = input("Date: ").strip()
        try:
            if "/" in date_str:
                month, day, year = map(int, date_str.split("/"))
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
            elif "," in date_str:
                parts = date_str.replace(",", "").split(" ")
                if len(parts) == 3:
                    month_name = parts[0]
                    day_str = parts[1]
                    year_str = parts[2]
                    if month_name.capitalize() in months:
                        month = months.index(month_name.capitalize()) + 1
                        day = int(day_str)
                        year = int(year_str)
                        if 1 <= day <= 31:
                            print(f"{year:04d}-{month:02d}-{day:02d}")
                            break
        except (ValueError, IndexError,EOFError):
            continue

if __name__ == "__main__":
    main()
