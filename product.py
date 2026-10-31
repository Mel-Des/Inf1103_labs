from abc import ABC, abstractmethod

class CanBeShipped(ABC):

    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class Product(ABC):

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        if self.__stock + quantity < 0:
            print("Insufficient stock.")
            return

        self.__stock += quantity

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
