from abc import ABC, abstractmethod

from supplier import Supplier

class Product(ABC):

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, transactions: list[dict] | None = None):
        self._product_id: str = str(product_id)
        self._name: str = str(name)
        self._price: float = float(price)
        self._stock: int = int(stock)
        self.supplier: Supplier = supplier
        self._transactions: list[dict] = (list(transactions) if transactions is not None else [])

        if self._price < 0:
            raise ValueError("Price cannot be negative.")

        if self._stock < 0:
            raise ValueError("Stock cannot be negative.")

    @property
    def price(self) -> float:
        return self._price

    def get_product_id(self) -> str:
        return self._product_id

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def get_stock(self) -> int:
        return self._stock

    def get_transactions(self) -> list[dict]:
        return self._transactions

    def update_stock(self, new_stock: int) -> None:
        new_stock = int(new_stock)
        if new_stock < 0:
            raise ValueError("Stock cannot be negative.")

        difference = new_stock - self._stock

        self._stock = new_stock

        self._transactions.append({
            "type": "STOCK_UPDATE",
            "quantity": difference,
            "amount": abs(difference) * self._price
        })

    def display_information(self) -> None:
        print(f"Product ID: {self._product_id}")
        print(f"Name: {self._name}")
        print(f"Price: ${self._price:.2f}")
        print(f"Stock Quantity: {self._stock}")
        print(f"Supplier: {self.supplier.name}")

    def record_initial_stock(self) -> None:
        self._transactions.append({
            "type": "ADD",
            "quantity": self._stock,
            "amount": self._price * self._stock
        })

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    def get_shipping_info(self) -> str:
        return "Shipping is not required."

    def to_dict(self) -> dict:
        return{
            "type": "product",
            "id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock,
            "supplier": self.supplier.to_dict(),
            "transactions": self._transactions
        }