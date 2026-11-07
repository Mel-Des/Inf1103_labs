from product import Product
from supplier import Supplier
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product):

    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier, transactions: list[dict] | None = None):
        super().__init__(product_id, name, price, stock, supplier, transactions)
        self.weight: float = float(weight)

        if self.weight < 0:
            raise ValueError("Weight cannot be negative.")

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.weight:.2f} Kg")

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return 2.00 + (1.50 * self.weight)

    def get_shipping_info(self) -> str:
        return f"Shipping Cost: ${self.calculate_shipping_cost():.2f}"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.weight
        return data

CanBeShipped.register(PhysicalProduct)