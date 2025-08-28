def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not s[:2].isalpha():
        return False
    if not 2 <= len(s) <= 6:
        return False
    i = 0
    while i < len(s):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            if not s[i:].isdigit():
                return False
            break
        i += 1
    if not s.isalnum():
        return False
    return True
if __name__ == "__main__":
    main()
