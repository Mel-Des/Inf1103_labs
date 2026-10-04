import json
import os

def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("Inventory loaded successfully.")
        return inventory

    else:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")
        return[]

def save_inventory(inventory):
    with open("inventory.json", "w")as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")

def display_all(inventory):
    print("\n========== INVENTORY ==========")

    if len(inventory) == 0:
        print("Inventory is empty.")

    else:
        for product in inventory:
            print(
                f"ID: {product['id']} | "
                f"Name {product['name']} | "
                f"Price: {product['price']:.2f} | "
                f"Stock: {product['stock']}"
                "------------------------------"
            )

def add_product(invetntory):

    
inventory = load_inventory()
display_all(inventory)
save_inventory(inventory)