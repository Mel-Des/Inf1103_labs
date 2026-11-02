from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):

    def __init__(self, product_id, name, price, stock, weight, transactions=None):
        super().__init__(product_id, name, price, stock, transactions)
        self.__weight = float(weight)

        if self.__weight < 0:
            raise ValueError("Weight cannot be negative.")

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight:.2f} Kg")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        return 2.00 + (1.50 * self.__weight)

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data