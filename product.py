from abc import ABC, abstractmethod

class CanBeShipped(ABC):

    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class Product(ABC):

    def __init__(self, product_id, name, price, stock, transactions=None):
        self._product_id = str(product_id)
        self._name = str(name)
        self._price = float(price)
        self._stock = int(stock)
        self._transactions = transactions if transactions is not None else []

        if self._price < 0:
            raise ValueError("Price cannot be negative.")

        if self._stock < 0:
            raise ValueError("Stock cannot be negative.")

    def get_product_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock

    def get_transactions(self):
        return self._transactions

    def update_stock(self, new_stock):
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

    def display_information(self):
        print("Product ID:", self.__product_id)
        print("Name:", self.__name)
        print("Price: $", self.__price)
        print("Stock Quantity:", self.__stock)

    @abstractmethod
    def get_fulfilment_info(self):
        pass

class PhysicalProduct(Product, CanBeShipped):

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print("Weight:", self.__weight, "Kg")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 2

class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print("Download Size:", self.download_size, "MB")

    def get_fulfilment_info(self):
        return "Delivered digitally."
