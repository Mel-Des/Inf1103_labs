import json
import os

inventory = {
    "products": [
        {
            "id": "P001",
            "name": "Laptop",
            "price": 1200.00,
            "stock": 15
        },
        {
            "id": "P002",
            "name": "Mouse",
            "price": 25.50,
            "stock": 40
        },
        {
            "id": "P003",
            "name": "Keyboard",
            "price": 45.00,
            "stock": 25
        }
    ],

    "transactions": []
}

def load_inventory():
    global inventory, transactions

    if os.path.exists("inventory.json"):
        print("inventory.json found.")
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        inventory.setdefault("transactions", [])
        print("Inventory loaded successfully.")
    else:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")

def save_inventory():
    with open("inventory.json", "w")as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")

def add_product():
    print("\nAdd New Product")

    pid = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    inventory["products"].append({
        "id": pid,
        "name": name,
        "price": price,
        "stock": stock
    })

    inventory["transactions"].append({
        "product_id": pid,
        "amount": stock,
    })

    print("\nProduct added successfully.")

def update_stock():
    print("\nUpdate Stock")
    pid = input("Enter Product ID: ")

    for product in inventory["products"]:
        if product["id"] == pid:
            print("\nProduct Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            new_stock = int(input("\nNew Stock Quantity:"))
            difference = new_stock - product["stock"]

            product["stock"] = new_stock

            inventory["transactions"].append({
                "product_id": pid,
                "amount": difference
            })

            print("\nStock updated successfully.")
            return

    print("\nProduct not found.")

def search_product():
    print("\nSearch Product")
    pid = input("Enter Product ID:")

    for product in inventory["products"]:
        if product["id"] == pid:
            print("\nProduct Found")
            print("-" * 50)
            print(
                f"ID: {product['id']} | "
                f"Name: {product['name']} | "
                f"Price: {product['price']:.2f} | "
                f"Stock: {product['stock']}"
            )
            print("-" * 50)
            return

    print("\nProduct not found.")


def display_all():
    print("\nCurrent Inventory")
    print("-" * 50)

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name {product['name']} | "
            f"Price: {product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 50)

def menu():

    print("\n---------- MENU ----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------")
    print("=" * 70)
    print("                 INVENTORY MANAGEMENT SYSTEM")
    print("=" * 70)

    load_inventory()

    while True:

        menu()

        option = input("\nEnter option: ")

        if option == "1":
            display_all()
        elif option == "2":
            add_product()
        elif option == "3":
            update_stock()
        elif option == "4":
            search_product()
        elif option == "5":
            print("\nSaving inventory...")
            save_inventory()
        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory()
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option.")