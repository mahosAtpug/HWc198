items = {"apple": 2, "banana": 1, "orange": 3, "bread": 2}

while True:
    total = 0.0
    cart = {}
    customer_name = input("Enter customer name: ")

    while True:
        print("Available items: ", ", ".join(items.keys()))
        item = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))

        if item in items:
            cart[item] = quantity
            total += items[item] * quantity
        else:
            print("Invalid item name!")

        repeat = input("Do you want to add more items? (Y/N): ")
        if repeat.upper() == "N":
            break

    print("\n************ BILL ************")
    print("Customer Name: ", customer_name)
    print("Items:")
    for item, quantity in cart.items():
        print(item, "\t", quantity, "\t", items[item] * quantity)
    print("Total: ", total)
    print("********************************\n")
    new_customer = input("Go to the next customer? (Y/N): ")
    if new_customer == "N":
        break

print("No more customers in line. Exiting...")
