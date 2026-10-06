import json
import os

FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "inventory.json"
)

inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15,
        "transactions": []
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40,
        "transactions": []
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25,
        "transactions": []
    }
]

def load_inventory():
    global inventory

    if os.path.exists(FILE_NAME):
        print("inventory.json found.")

        file =  open(FILE_NAME, "r")
        data = json.load(file)
        file.close()

        inventory = data["inventory"]

        for product in inventory:
            if "transactions" not in product:
                product["transactions"] = []

        print("Inventory loaded successfully.")
    else:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")

def save_inventory():
    data = {
        "inventory": inventory
    }

    file = open(FILE_NAME, "w")
    json.dump(data, file, indent=4)
    file.close()

def add_product():
    print("\nAdd New Product")

    pid = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    product = {
        "id": pid,
        "name": name,
        "price": price,
        "stock": stock,
        "transactions": []
    }

    transaction = {
        "type": "ADD",
        "quantity": stock,
        "amount": price * stock
    }

    product["transactions"].append(transaction)

    inventory.append(product)

    print("\nProduct added successfully.")

def update_stock():
    print("\nUpdate Stock")
    pid = input("Enter Product ID: ")

    product = search_product(pid)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")

    new_stock = int(input("\nNew Stock Quantity:"))
    difference = new_stock - product["stock"]

    product["stock"] = new_stock

    transaction = {
        "type": "STOCK_UPDATE",
        "quantity": difference,
        "amount": abs(difference) * product["price"]
    }

    product["transactions"].append(transaction)

    print("\nStock updated successfully.")

def search_product(product_id):
    if product_id is None:
        product_id = input("Enter Product ID:")

    for product in inventory:
        if product["id"] == product_id:
            return product

    return None

def display_all():
    print("\nCurrent Inventory")
    print("-" * 50)

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 50)

def menu():

    while True:

        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("------------------------")

        option = input("\nEnter option: ")

        if option == "1":
            display_all()
        elif option == "2":
            add_product()
        elif option == "3":
            update_stock()
        elif option == "4":
            print("\nSearch Product")
            product_id = input("Enter Product ID: ")
            product = search_product(product_id)
            if product is not None:
                print("\nProduct Found")
                print("----------------------------------------------")
                print(f"ID: {product['id']}")
                print(f"Name: {product['name']}")
                print(f"Price: ${product['price']:.2f}")
                print(f"Stock: {product['stock']}")
                print("----------------------------------------------")

            else:
                print("\nProduct not found.")
        elif option == "5":
            print("\nSaving inventory...")
            save_inventory()
            print("Inventory saved successfully to inventory.json.")
        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory()
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break

def main():
    print("=" * 50)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)

    print()

    load_inventory()

    menu()

main()