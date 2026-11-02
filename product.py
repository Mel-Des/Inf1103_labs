from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, product_id, name, price, stock, transactions=None):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)
        self.__transactions = transactions if transactions is not None else []

        if self.__price < 0:
            raise ValueError("Price cannot be negative.")

        if self.__stock < 0:
            raise ValueError("Stock cannot be negative.")

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def get_transactions(self):
        return self.__transactions.copy()

    def update_stock(self, new_stock):
        new_stock = int(new_stock)
        if new_stock < 0:
            raise ValueError("Stock cannot be negative.")

        difference = new_stock - self.__stock

        self.__stock = new_stock

        self.__transactions.append({
            "type": "STOCK_UPDATE",
            "quantity": difference,
            "amount": abs(difference) * self.__price
        })

    def display_information(self):
        print("Product ID:", self.__product_id)
        print("Name:", self.__name)
        print(f"Price: ${self.__price:.2f}")
        print("Stock Quantity:", self.__stock)

    def record_initial_stock(self):
        self.__transactions.append({
            "type": "ADD",
            "quantity": self.__stock,
            "amount": self.__price * self.__stock
        })

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    def to_dict(self):
        return{
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "transactions": self.__transactions
        }