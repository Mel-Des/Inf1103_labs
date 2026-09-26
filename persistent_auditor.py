def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            return 0,[]

        total = float(lines[0].strip())

        history = []
        for line in lines[1:]:
            if line.strip() != "":
                history.append(float(line.strip()))
        return total, history
    except FileNotFoundError:
        return 0,[]

def load_orders():
    orders = []

    try:
        with open("orders.txt", "r") as file:
            for line in file:
                orders.append(line.strip())

    except FileNotFoundError:
        pass
    return orders

def save_order(order):
    with open("orders.txt", "a") as file:
        file.write(order + "\n")

def main():
    total, transaction_history = load_inventory()
    orders = load_orders()

    print("Current Orders:")
    print()

    for order in orders:
        print(order)

    print()

    while True:
        product_name = input("Enter Product Name: ")

        if product_name.lower() == "quit":
            break

        quantity = int(input("Enter Quantity: "))

        if len(orders) == 0:
            order_id = 1001
        else:
            last_order = orders[-1]
            order_id = int (last_order.split(",")[0]) + 1

        new_order = str(order_id) + "," + product_name + "," + str(quantity)
        orders.append(new_order)

        total += quantity
        transaction_history.append(quantity)

        print()
        print("New Order Added:")
        print(new_order)

        print()
        print("Transaction History:")
        print(transaction_history)

        save_order(new_order)

        print()
        print("Order Successfully saved to orders.txt")
        print()

if __name__ == "__main__":
    main()