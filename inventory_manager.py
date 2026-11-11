import json
import os

from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
from inventory import Inventory
from order import Order

FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "inventory.json"
)

def product_from_dict(item: dict) -> Product:
    supplier_data = item.get("supplier", {})

    supplier = Supplier(
        supplier_data.get("supplier_id", "S001"),
        supplier_data.get("name", "ABC Supplier"),
        supplier_data.get("contact_email", "ABC@example.com")
    )

    transactions = item.get("transactions", [])

    product_type = item.get("type", "physical")

    if product_type == "physical":
        return PhysicalProduct(
            item["id"],
            item["name"],
            item["price"],
            item["stock"],
            item.get("weight", 0.0),
            supplier,
            transactions
        )

    elif product_type == "digital":
        return DigitalProduct(
            item["id"],
            item["name"],
            item["price"],
            item["stock"],
            item.get("download_size", 0.0),
            supplier,
            transactions
        )

    else:
        raise ValueError("Invalid product type: " + product_type)

def load_inventory() -> Inventory:
    inventory = Inventory()

    if not os.path.exists(FILE_NAME):
        return inventory

    with open(FILE_NAME, "r") as file:
        data =json.load(file)

    for item in data.get("inventory", []):
        product = product_from_dict(item)
        inventory.add_product(product)

    return inventory

def save_inventory(inventory: Inventory) -> None:
    data = {
        "inventory": [
            product.to_dict()
            for product in inventory.get_all_products()
        ]
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully to inventory.json.")

def add_product(inventory: Inventory) -> None:
    print("\nAdd New Product")
    print("-" * 40)

    product_id = input("Enter Product ID: ")

    if inventory.find_product(product_id) is not None:
        print("Product ID already exists.")
        return

    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: $"))
    stock = int(input("Enter Product Stock: "))

    print("\nSelect Product Type")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Choose product type (1 or 2): ")

    print("\n--- Supplier Information ---")

    supplier_id = input("Enter Supplier ID: ")
    supplier_name = input("Enter Supplier Name: ")
    supplier_email = input("Enter Supplier Email: ")

    supplier = Supplier(
        supplier_id,
        supplier_name,
        supplier_email
    )

    if product_type == "1":
        weight = float(input("Weight (Kg): "))

        if weight < 0:
            print("Weight cannot be negative.")
            return

        product = PhysicalProduct(
            product_id, name, price, stock, weight, supplier
        )

    elif product_type == "2":
        download_size = float(input("Download Size (MB): "))

        if download_size < 0:
            print("Download size cannot be negative.")
            return

        product = DigitalProduct(
            product_id, name, price, stock, download_size, supplier
        )

    else:
        print("Invalid product type.")
        return

    product.record_initial_stock()

    inventory.add_product(product)
    save_inventory(inventory)

    print("\nProduct added successfully.")

def display_products(inventory: Inventory) -> None:
    inventory.display_all()

def update_stock(inventory: Inventory) -> None:
    print("\nUpdate Stock")
    pid = input("Enter Product ID: ").strip()

    product = inventory.search_product(pid)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    print("Name:", product.get_name())
    print("Current Stock:", product.get_stock())

    new_stock = int(input("\nNew Stock Quantity: "))

    if new_stock < 0:
        print("Stock cannot be negative.")
        return

    product.update_stock(new_stock)

    save_inventory(inventory)

    print("\nStock updated successfully.")

def search_product(inventory: Inventory) -> None:
    print("\nSearch Product")
    pid = input("Enter Product ID: ").strip()

    product = inventory.search_product(pid)

    if product is not None:
        print("\nProduct found")
        print("-" * 50)
        product.display_information()

        print("Fulfilment:", product.get_fulfilment_info())

        if product.product_type == "physical":
            print(
                "Shipping Cost: $",
                f"{product.calculate_shipping_cost():.2f}"
            )
        print("-" * 50)

    else:
        print("\nProduct not found.")

def remove_product(inventory: Inventory) -> None:
    print("\nRemove Product")

    product_id = input("Enter Product ID: ")

    removed = inventory.remove_product(product_id)

    if removed:
        save_inventory(inventory)
        print("Product removed successfully.")
    else:
        print("Product not found.")

def create_order(inventory: Inventory) -> None:
    print("\nCreate Order")

    order_id = input("Enter Order ID: ")

    order = Order(order_id)

    while True:
        product_id = input("Enter Product ID (or 'done' to finish): ")

        if product_id.lower() == "done":
            break

        product = inventory.find_product(product_id)

        if product is None:
            print("Product not found.")
            continue

        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        if quantity > product.get_stock():
            print("Not enough stock available.")
            continue

        order.add_order_line(product, quantity)

        print("Product added to order.")

    if len(order.order_lines) == 0:
        print("No products were added to the order.")
        return

    print("\nOrder Summary:")

    order.display_order()

    print(f"Total Amount: ${order.calculate_total():.2f}")

def menu() -> None:
    inventory = load_inventory()

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Remove Product")
        print("6. Create Order")
        print("7. Save Inventory")
        print("8. Exit")
        print("------------------------")

        option = input("\nEnter option: ").strip()

        if option == "1":
            display_products(inventory)

        elif option == "2":
            add_product(inventory)

        elif option == "3":
            update_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            remove_product(inventory)

        elif option == "6":
            create_order(inventory)

        elif option == "7":
            print("\nSaving inventory...")
            save_inventory(inventory)

        elif option == "8":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)

            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("\nInvalid option. Please enter 1 to 6.")

def main() -> None:
    print("=" * 50)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)
    menu()

if __name__ == "__main__":
    main()