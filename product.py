from abc import ABC, abstractmethod

class CanBeShipped(ABC):

    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class Product(ABC):

    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def update_stock(self, new_stock):
        if new_stock < 0:
            raise ValueError("Stock cannot be negative.")

        self.__stock = new_stock

    def display_information(self):
        print(f"ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock Quantity: {self.stock}")

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    def to_dict(self):
        return{
            "id": self.product_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
        }

class PhysicalProduct(Product):

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.weight = float(weight)

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.weight} Kg")

    def get_fulfilment_info(self):
        return "Requires physical shipping."

    def calculate_shipping_cost(self):
        return 2.00 + (1.50 * self.weight)

    def to_dict(self):
        data = super().to_dict()

        data["type"] = "physical"
        data["weight"] = self.weight

        return data

class DigitalProduct(Product):

    def __init__(
            self, product_id, name, price, stock, download_size
    ):
        super().__init__(product_id, name, price, stock)
        self.download_size = float(download_size)

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.download_size} MB")

    def get_fulfilment_info(self):
        return "Delivered digitally."

    def to_dict(self):
        data = super().to_dict()

        data["type"] = "digital"
        data["download_size"] = self.download_size

        return data

CanBeShipped.register(PhysicalProduct)