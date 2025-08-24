def main():
    name = input("camelCase: ")
    snake_case = ""
    for char in name:
        if char.isupper():
            snake_case += "_" +char.lower()
        else:
            snake_case += char
    print(f"snake_case:{snake_case}")

if __name__ == "__main__":
    main()


