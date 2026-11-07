from product import Product

class Inventory:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        if self.find_product(product.get_product_id()) is not None:
            raise ValueError("Product ID already exists.")

        self.products.append(product)

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_product_id() == product_id:
                return product

        return None

    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def remove_product(self, product_id: str) -> bool:
        product = self.find_product(product_id)

        if product is None:
            return False

        self.products.remove(product)
        return True

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        print("-" * 50)

        if not self.products:
            print("No products in inventory.")

        for product in self.products:
            product.display_information()

            print("Fulfilment:", product.get_fulfilment_info())
            print(product.get_shipping_info())

            print("-" * 50)

    def get_all_products(self) -> list[Product]:
        return self.products.copy()
    