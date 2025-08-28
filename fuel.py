def main():
    fraction = get_fraction()
    percentage = round(fraction * 100)

    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage}%")

def get_fraction():
    while True:
        try:
            fraction_str = input("Fraction: ")
            numerator_str, denominator_str = fraction_str.split('/')

            numerator = int(numerator_str)
            denominator = int(denominator_str)
            if numerator < 0 or denominator < 0:
                raise ValueError("Numerator and denominator must be non-negative.")

            if numerator > denominator:
                print("Numerator cannot be greater than the denominator. Please try again.")
                continue

            return numerator / denominator

        except ValueError:
            print("Invalid input. Please enter a valid fraction in the format X/Y, where X and Y are integers.")
        except ZeroDivisionError:
            print("The denominator cannot be zero. Please try again.")
        except IndexError:
            print("Invalid format. Please enter a fraction in the format X/Y.")

if __name__ == "__main__":
    main()
