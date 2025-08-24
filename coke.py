#Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents
# and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
# implement a program that prompts the user to insert a coin, one at a time,
# each time informing the user of the amount due. Once the user has inputted at least 50 cents,
# output how many cents in change the user is owed. Assume that the user will only input integers,
# and ignore any integer that isn’t an accepted denomination.

amount_due = 50
added_coins = 0
print(f"Amount Due: {amount_due} ")
while True:
    coin = int(input("Insert Coin: "))
    if coin in [25,10,5] and amount_due >0:
        amount_due = amount_due - coin
        added_coins = added_coins + coin
    if amount_due <= 0:
        change_owed = abs(amount_due)
        print(f"Change Owed: {change_owed}")
        break
    else:
        print(f"Amount Due: {amount_due}")
