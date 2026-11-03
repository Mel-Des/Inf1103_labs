import json
import os

from product import PhysicalProduct, DigitalProduct
from inventory import Inventory

FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "inventory.json"
)

def product_from_dict(item):
    transactions = item.get("transactions", [])

    product_type = item.get("type", "physical")

    if product_type == "physical":
        return PhysicalProduct(
            item["id"],
            item["name"],
            item["price"],
            item["stock"],
            item.get("weight", 0.0),
            transactions
        )

    elif product_type == "digital":
        return DigitalProduct(
            item["id"],
            item["name"],
            item["price"],
            item["stock"],
            item.get("download_size", 0.0),
            transactions
        )

    else:
        raise ValueError("Unknown product type: " + product_type)

def load_inventory(inventory):
    if not os.path.exists(FILE_NAME):
        print("inventory.json not found.")
        print("Starting with an empty inventory.")
        return

    print("inventory.json found.")

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        data =json.load(file)

    for item in data.get("inventory", []):
        product = product_from_dict(item)
        inventory.add_product(product)

    print("Inventory loaded successfully.")

def save_inventory(inventory):
    data = {
        "inventory": [
            product.to_dict()
            for product in inventory.get_all_products()
        ]
    }

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def add_product(inventory):
    print("\nAdd New Product")

    pid = input("Product ID: ").strip()
    name = input("Product Name: ").strip()
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    if pid == "" or name == "":
        print("Product ID and name cannot be empty.")
        return

    if price < 0 or stock < 0:
        print("Price and Stock cannot be negative.")
        return

    product = Product(pid, name, price, stock)
    product.record_initial_stock()

    inventory.add_product(product)

    print("\nProduct added successfully.")

def update_stock(inventory):
    print("\nUpdate Stock")
    pid = input("Enter Product ID: ").strip()

    product = inventory.search_product(pid)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")

    new_stock = int(input("\nNew Stock Quantity: "))

    if new_stock < 0:
        print("Stock cannot be negative.")
        return

    product.update_stock(new_stock)

    print("\nStock updated successfully.")

def search_product(inventory):
    print("\nSearch Product")
    pid = input("Enter Product ID: ").strip()

    product = inventory.search_product(pid)

    if product is not None:
        print("\nProduct found")
        print("-" * 50)
        product.display_information()
        print("-" * 50)

    else:
        print("\nProduct not found.")

def menu(inventory):
    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("------------------------")

        option = input("\nEnter option: ").strip()

        if option == "1":
            inventory.display_all()

        elif option == "2":
            add_product(inventory)

        elif option == "3":
            update_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            print("\nSaving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.")

        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")

            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("\nInvalid option. Please enter 1 to 6.")

def main():
    print("=" * 50)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)

    inventory = Inventory()

    load_inventory(inventory)
    menu(inventory)

if __name__ == "__main__":
    main()