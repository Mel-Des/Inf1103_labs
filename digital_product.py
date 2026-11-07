from product import Product
from supplier import Supplier

class DigitalProduct(Product):

    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier, transactions: list[dict] | None = None):
        super().__init__(product_id, name, price, stock, supplier, transactions)
        self.download_size: float = float(download_size)

        if self.download_size < 0:
            raise ValueError("Download size cannot be negative.")

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.download_size:.2f} MB")

    def get_fulfilment_info(self) -> str:
        return "Delivered digitally."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.download_size
        return data