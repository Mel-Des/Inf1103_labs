class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            raise ValueError("Product ID already exists.")

        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("-" * 50)

        if not self.__products:
            print("No products in inventory.")

        for product in self.__products:
            print(
                f"ID: {product.get_product_id()} | "
                f"Name: {product.get_name()} | "
                f"Price: {product.get_price():.2f} | "
                f"Stock: {product.get_stock()}"
            )

        print("-" * 50)

    def get_all_products(self):
        return self.__products.copy()
    