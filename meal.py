def main():
    timeofday = input("What time is it? ")
    time = convert(timeofday)
    if time <= 8.0 >=7.0:
        print("breakfast time")
    elif time <= 13 >= 12.0:
        print("lunch time")
    elif time <=19.0 >=18.0:
        print("dinner time")

def convert(time):
    hrs , min = time.split(":")
    hr_float = float(hrs)
    min_float = float(min)
    total_hrs = hr_float + min_float / 60
    return total_hrs


if __name__ == "__main__":
    main()
