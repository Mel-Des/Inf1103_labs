inventory = [
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

def display_all():
    print("\nCurrent Inventory")
    print("-" * 55)

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name {product['name']} | "
            f"Price: {product['price']:.2f} | "
            f"Stock: {product['stcok']}"
        )

    print("-" * 55)

display_all()