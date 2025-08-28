def main():
    grocery = grocery_list()
    print_groceries(grocery)
def grocery_list():
    items = {}
    while True:
        try:
            item = input().strip().upper()
            if not item:
                continue
            items[item] = items.get(item, 0) + 1
        except EOFError:
            break
    return items
def print_groceries(items):
    sorted_items = sorted(items.keys())
    for item in sorted_items:
        print(f"{items[item]} {item}")
if __name__ == "__main__":
    main()

