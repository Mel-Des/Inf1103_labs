import json
import os

[
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15,
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40,
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25,
    }
]

def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("Inventory loaded successfully.")
        return inventory

    else:
        print("inventory.json not found.")
        return[]

def display_all(inventory):
    print("\nCurrent Inventory")
    print("-" * 55)

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name {product['name']} | "
            f"Price: {product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 55)

inventory = load_inventory()
display_all(inventory)