import json
import os

from product import Product
from inventory import Inventory

FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "inventory.json"
)

def load_inventory(inventory):
    if not os.path.exists(FILE_NAME):
        print("inventory.json not found.")
        print("Starting with an empty inventory.")

        inventory.add_product(
            Product("P001", "Laptop", 1200.00, 15)
        )

        inventory.add_product(
            Product("P002", "Mouse", 25.50, 40)
        )

        inventory.add_product(
            Product("P003", "Keyboard", 45.00, 25)
        )
        return

    print("inventory.json found.")

    with open(FILE_NAME, "r") as file:
        data =json.load(file)

    for item in data["inventory"]:
        product = Product(
            item["id"],
            item["name"],
            item["price"],
            item["stock"],
            item.get("transactions", [])
        )

        inventory.add_product(product)

    print("Inventory loaded successfully.")

def save_inventory(inventory):
    data = {
        "inventory": [
            product.to_dict()
            for product in inventory.get_all_products()
        ]
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)